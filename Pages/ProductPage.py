from selenium.webdriver.common.by import By


class ProductPageLocators:
    PRODUCT_TITLE = (By.CLASS_NAME, 'bgnone')


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def getProductTitle(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_TITLE)
