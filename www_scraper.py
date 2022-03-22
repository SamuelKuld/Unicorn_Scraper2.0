from bs4 import BeautifulSoup
import time
import logger
import requester
import iterator_module


class Scraper():
    def __init__(self, start='aa'):
        self.word = iterator_module.Keyword(start)

    def get_url(self):
        return f"http://{self.word.word}.com"

    def get_all_data(self):
        return requester.get_page(self.get_url())

    def save_as_page(self):
        try:
            data = self.get_all_data()
            if not data == None:
                logger.info("Www scraper",
                            f"Getting and saving page {self.word.word}")
                with open(f"www_html/{self.word.word}.html", "w+") as file:
                    file.write("")
                with open(f"www_html/{self.word.word}.html", "a+") as file:
                    file.write(data)
        except UnicodeEncodeError:
            pass

    def tick(self):
        self.word.tick_with_adding()


if __name__ == "__main__":
    scraper = Scraper('a')
    scraper.save_as_page()
    scraper.tick()
    scraper.save_as_page()
