import requester
import time
import www_scraper
import istockphoto
import threading
import logger


def save_istock_iterations(iterations):
    with open("istock_iter.txt", "w+") as file:
        file.write(str(iterations))


def save_www_iterations(iterations):
    with open("www_iter.txt", "w+") as file:
        file.write(str(iterations))


def load_istock_iterations():
    with open("istock_iter.txt", "r") as file:
        data = file.read()

    return int(data)


def load_www_iterations():
    with open("www_iter.txt", "r") as file:
        data = file.read()

    return int(data)


def istock_photo_loop():
    iterations = load_istock_iterations()
    scraper = istockphoto.Scraper()
    for i in range(iterations):
        scraper.tick()
    while True:
        scraper.tick()
        iterations += 1
        scraper.save_as_page()
        time.sleep(3)
        save_istock_iterations(iterations)


def www_photo_loop():
    iterations = load_istock_iterations()
    scraper = www_scraper.Scraper()
    for i in range(iterations):
        scraper.tick()
    while True:
        try:
            scraper.save_as_page()
        except requester.non_200_response:
            logger.info(
                "Main - Www loop", f"Could not get page {scraper.word.word}, ticking and trying the next")
        iterations += 1
        scraper.tick()
        save_www_iterations(iterations)
        time.sleep(3)


class Thread(threading.Thread):
    def __init__(self, name, function_):
        threading.Thread.__init__(self)
        self.function_ = function_
        self.name = name

    def run(self):
        logger.info("Main", f"Starting Thread {self.name}")
        self.function_()


if __name__ == "__main__":
    working = True
    if working:
        istock_loop = Thread("istock_loop", istock_photo_loop)
        www_loop = Thread("www_loop", www_photo_loop)
        istock_loop.start()
        www_loop.start()
    else:
        print("Gotta fix something")
