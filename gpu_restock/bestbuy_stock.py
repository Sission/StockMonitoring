from selenium import webdriver
from gpu_restock.basic import Colors
from datetime import datetime
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from prettytable import PrettyTable


class StockChecking(webdriver.Chrome):
    def __init__(self, url, teardown=False):
        self.PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        self.DRIVER_PATH = os.path.join(self.PROJECT_ROOT, "../SeleniumDrivers/chromedriver")
        self.teardown = teardown
        self.url = url
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f'user-agent={user_agent}')

        super(StockChecking, self).__init__(executable_path=self.DRIVER_PATH, options=options)
        self.implicitly_wait(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_page(self):
        self.get(self.url)

    def info(self):
        print('Checking ......')
        title = self.find_element(By.CLASS_NAME, "sku-title").text
        print(title)

        print(Colors.HEADER + 'Price:' + Colors.ENDC, end=" ")
        price = self.find_element(
            By.CSS_SELECTOR, 'div[class="priceView-hero-price priceView-customer-price"').find_element(
            By.CSS_SELECTOR, 'span[aria-hidden="true"]'
        ).get_attribute("innerHTML")
        print(price)

    def run(self):
        self.info()
        status = self.find_element(
            By.CSS_SELECTOR, 'div[class="fulfillment-add-to-cart-button"]'
        ).text
        no_stock = ['no', 'not', 'sold', 'out']
        in_stock = ['cart', 'add']
        if bool([ele for ele in no_stock if (ele in status.lower())]):
            print(Colors.HEADER + 'Status: ' + Colors.WARNING + 'Out of Stock' + Colors.ENDC)
        elif bool([ele for ele in in_stock if (ele in status.lower())]):
            print(Colors.HEADER + 'Status: ' + Colors.OKGREEN + 'In Stock !!' + Colors.ENDC)
        else:
            print(Colors.WARNING + "Can't get the status" + Colors.ENDC)
