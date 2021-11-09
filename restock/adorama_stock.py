from selenium import webdriver


class AdoramaStock(webdriver.Chrome):
    def __init__(self, url, merchant, st, teardown=False):
        self.st = st
        self.teardown = teardown
        self.url = url
        self.st.merchant = merchant
        super(AdoramaStock, self).__init__(executable_path=st.DRIVER_PATH, options=st.options)
        self.implicitly_wait(2)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load_page(self):
        self.get(self.url)

    # def info(self):
    #     print('Checking ......')
    #     title = self.find_element(By.CLASS_NAME, "primary-info cf clear").text
    #     print(title)
    #
    #     print(Colors.HEADER + 'Price:' + Colors.ENDC, end=" ")
    #     price = self.find_element(
    #         By.CSS_SELECTOR, 'div[class="priceView-hero-price priceView-customer-price"').find_element(
    #         By.CSS_SELECTOR, 'span[aria-hidden="true"]'
    #     ).get_attribute("innerHTML")
    #     print(price)
    #
    # def run(self):
    #     element = self.find_element(By.CSS_SELECTOR, '#px-captcha')
    #     action = ActionChains(self)
    #     action.click_and_hold(element)
    #     action.perform()
    #     print('pressing')
    #     time.sleep(10)
    #     action.release(element)
    #     action.perform()
    #     time.sleep(0.2)
    #     action.release(element)
    #     print('end')
    #
    #     self.info()
    #     status = self.find_element(
    #         By.CSS_SELECTOR, 'div[class="fulfillment-add-to-cart-button"]'
    #     ).text
    #     no_stock = ['no', 'not', 'sold', 'out']
    #     in_stock = ['cart', 'add']
    #     if bool([ele for ele in no_stock if (ele in status.lower())]):
    #         print(Colors.HEADER + 'Status: ' + Colors.WARNING + 'Out of Stock' + Colors.ENDC)
    #     elif bool([ele for ele in in_stock if (ele in status.lower())]):
    #         print(Colors.HEADER + 'Status: ' + Colors.OKGREEN + 'In Stock !!' + Colors.ENDC)
    #     else:
    #         print(Colors.WARNING + "Can't get the status" + Colors.ENDC)
