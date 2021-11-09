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
from selenium.common.exceptions import NoSuchElementException


class MicroCenterStock(webdriver.Chrome):
    def __init__(self, url, merchant, st, teardown=False):
        self.st = st
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
        staleElement = True
        while staleElement:
            try:
                location = self.find_element(By.CSS_SELECTOR, 'li[class="dropdown-itemLI store_121"]')
                location.click()
                staleElement = False
            except (Exception,):
                staleElement = True

    def load_page(self):
        self.get(self.url)
        try:
            self.find_element(By.ID, "storeInfoChange").find_element(By.CLASS_NAME, "pre-dropdown.boosted")
            # print('Have shown window')
            try:
                location_expand = self.find_element(By.ID, 'selectedStoreChangeAjax')
                # print('Location chosen, choose a different location')
                location_expand.click()
                # print('expand location')
            except (Exception,):
                # print('No Location chosen, choose a location')
                pass
            self.choose_location()
        except (Exception,):
            # print('No shown window')
            pass

    def info(self):
        title = self.find_element(By.XPATH, '//div[@class="mm-t007-title"]//span[@data-position="5"]').get_attribute('innerHTML')
        self.st.item = title

        price = self.find_element(By.ID, "pricing").get_attribute('content')
        self.st.price = f'${price}'

    #
    def run(self, current_time):
        self.info()
        self.st.time = current_time
        status = self.find_element(
            By.CLASS_NAME, 'inventory'
        ).text
        self.st.availability = status
