from selenium.webdriver.common.by import By

class AccountPageLocators:
    TITLE = (By.CSS_SELECTOR, 'h1[class="heading1"]')

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(*AccountPageLocators.TITLE)
