from selenium import webdriver
import restock.basic
from restock.basic import Colors, Setting
from datetime import datetime
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from prettytable import PrettyTable
from selenium.webdriver.common.action_chains import ActionChains


class MicroCenterStock(webdriver.Chrome):
    def __init__(self, url, merchant, teardown=False):
        self.st = Setting()
        self.teardown = teardown
        self.url = url
        self.st.merchant = merchant
        super(MicroCenterStock, self).__init__(executable_path=self.st.DRIVER_PATH, options=self.st.options)
        self.implicitly_wait(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def choose_location(self):
        # Change the store location here
        location = self.find_element(By.CSS_SELECTOR, 'li[class="dropdown-itemLI store_121"]')
        location.click()

    def load_page(self):
        self.get(self.url)
        self.choose_location()

    def info(self,current_time):
        title = self.find_element(By.XPATH, '//div[@class="mm-t007-title"]//span[@data-position="5"]').get_attribute('innerHTML')
        self.st.item = title

        price = self.find_element(By.ID, "pricing").get_attribute('content')
        self.st.price = f'${price}'

    #
    def run(self, current_time):
        self.info(current_time)
        self.st.time = current_time
        status = self.find_element(
            By.CLASS_NAME, 'inventory'
        ).text
        self.st.availability = status

