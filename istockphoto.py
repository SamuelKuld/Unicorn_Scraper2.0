from bs4 import BeautifulSoup
import time
import logger
import requester
import iterator_module


class Scraper():
    def __init__(self, start=''):
        self.word = iterator_module.Keyword(start)

    def get_url(self):
        return f"https://www.istockphoto.com/search/2/image?phrase={self.word.word}&page=1"

    def get_all_images(self):
        data = BeautifulSoup(
            requester.get_page(
                self.get_url()), features="html.parser")
        data = data.find(attrs={"data-testid": "gallery-items-container"})
        return "".join(str(data))

    def save_as_page(self):
        logger.info("Istock scraper",
                    f"Getting and saving page {self.word.word}")
        with open(f"istock_html/{self.word.word}.html", "w+") as file:
            file.write(
                "<body style='background-color:black; justify-content:center; text-align:center; margin-left:20%; margin-right:20%'>")
        with open(f"istock_html/{self.word.word}.html", "a+") as file:
            file.write(self.get_all_images())
            file.write("</body>")

    def tick(self):
        self.word.tick_with_adding()


if __name__ == "__main__":
    scraper = Scraper('a')
    scraper.save_as_page()
    scraper.tick()
    scraper.save_as_page()
