import requests
import logger


class non_200_response(Exception):
    def __init__(self, message="Response Value not 200"):
        super(non_200_response, self).__init__(message)


def get_data(url):
    try:
        session = requests.Session()
        response = requests.get(
            url,
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "referer": "https://duckduckgo.com/",
            },
        )
        if response.status_code != 200:
            session.close()
            raise non_200_response(
                f"Response Value Not 200 ; Response = {response.status_code}")
        return response.text

    except Exception as e:
        logger.error(
            "Requester", f"When attempting to get data from URL: {url}; {e}")


def get_page(url):
    return get_data(url)
