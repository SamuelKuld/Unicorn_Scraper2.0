import logging

log_name = "app.log"

logging.basicConfig(
    level=logging.ERROR,
    filename=log_name,
    filemode="a",
    format=f"\n[%(asctime)s] : %(levelname)s - %(message)s\n",
)


def error(name, text: str):
    print(f"[{name}] ERROR : {text}")
    logging.exception(text)


def info(name, text: str):
    print(f"[{name}] Info : {text}")
    logging.info(text)


def warning(name, text: str):
    print(f"[{name}] : Warning : {text}")
    logging.warning(text)
