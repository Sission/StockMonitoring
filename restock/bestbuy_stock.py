from selenium import webdriver
from restock.basic import Colors, Setting
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from prettytable import PrettyTable


class BestBuyStock(webdriver.Chrome):
    def __init__(self, url, merchant, teardown=False):
        self.st = Setting()
        self.teardown = teardown
        self.url = url
        self.st.merchant = merchant
        super(BestBuyStock, self).__init__(executable_path=self.st.DRIVER_PATH, options=self.st.options)
        self.implicitly_wait(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_page(self):
        self.get(self.url)

    def info(self, current_time):
        item = self.find_element(By.CLASS_NAME, "sku-title").text
        self.st.item = item
        # print(item)

        # print(f'[{current_time}]' + Colors.HEADER + ' Price:' + Colors.ENDC, end=" ")
        price = self.find_element(
            By.CSS_SELECTOR, 'div[class="priceView-hero-price priceView-customer-price"').find_element(
            By.CSS_SELECTOR, 'span[aria-hidden="true"]'
        ).get_attribute("innerHTML")
        self.st.price = price
        # print(price)

    def run(self, current_time):
        self.info(current_time)
        self.st.time = current_time
        status = self.find_element(
            By.CSS_SELECTOR, 'div[class="fulfillment-add-to-cart-button"]'
        ).text
        self.st.availability = status
        # self.st.rt_status(status, current_time)

