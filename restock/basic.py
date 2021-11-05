from selenium import webdriver
import os


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
    def __init__(self):
        self.PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        self.DRIVER_PATH = os.path.join(self.PROJECT_ROOT, "../SeleniumDrivers/chromedriver")
        self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("--headless")
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--incognito")
        self.no_stock = ['no', 'not', 'sold', 'out']
        self.in_stock = ['cart', 'add']
        self.time = None
        self.item = None
        self.merchant = None
        self.price = None
        self.availability = None

    def rt_status(self, status, current_time):

        if bool([ele for ele in self.no_stock if (ele in status.lower())]):
            print(f'[{current_time}]' + Colors.HEADER + ' Status: ' + Colors.WARNING + 'Out of Stock' + Colors.ENDC)
        elif bool([ele for ele in self.in_stock if (ele in status.lower())]):
            print(f'[{current_time}]' + Colors.HEADER + ' Status: ' + Colors.OKGREEN + 'In Stock !!' + Colors.ENDC)
        else:
            print(f'[{current_time}]' + Colors.WARNING + " Can't get the status" + Colors.ENDC)
