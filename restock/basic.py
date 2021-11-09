from selenium import webdriver
import os
from colorama import init
import telegram
from datetime import datetime

init()


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Setting:
    def __init__(self, OS):
        self.PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        if OS == 'Windows':
            self.DRIVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, r'SeleniumDrivers/Windows/chromedriver.exe'))
        else:
            self.DRIVER_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, f'SeleniumDrivers/{OS}/chromedriver'))

        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--incognito")
        self.options.add_argument("--no-sandbox")
        self.no_stock = ['no', 'not', 'sold', 'out']
        self.in_stock = ['cart', 'add']
        self.time = None
        self.item = None
        self.merchant = None
        self.price = None
        self.availability = None
        self.no_stock = ['no', 'not', 'sold', 'out']
        self.in_stock = ['cart', 'add']

    def status_check(self, availability):
        if bool([ele for ele in self.no_stock if (ele in availability.lower())]):
            avail = 0
        elif bool([ele for ele in self.in_stock if (ele in availability.lower())]):
            avail = 1
        else:
            avail = 2
        return avail


def telegram_info(file):
    with open(file) as f:
        url = f.readlines()
        url = [line.rstrip() for line in url]
    api_key = url[0].split("'", 1)[1].split("'", 1)[0]
    user_id = url[1].split("'", 1)[1].split("'", 1)[0]
    return api_key, user_id


def telegram_communicator(api_key, user_id, info):
    bot = telegram.Bot(token=api_key)
    bot.send_message(chat_id=user_id, text=info)
    return datetime.now().hour
