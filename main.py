import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise


if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather?city=Addis%20Ababa&country=ET')
    if r.status_code == 200:
        data = r.json()
        temperature0 = data["forecast"]["temp"]
        temperature1 = data["forecast"]["pressure"]
        temperature2 = data["forecast"]["humidity"]
        temperature3 = data["weather"]["category"]
        logger.info(f'Weather in Addis Ababa: 🌡️ {temperature0} °C, 💨 {temperature1} hPa, 💦 {temperature2} %rh, 🌦️ {temperature3}')
