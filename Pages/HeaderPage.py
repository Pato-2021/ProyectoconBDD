from selenium.webdriver.common.by import By


class HeaderPageLocators:
    SEARCH_INPUT = (By.ID, 'filter_keyword')
    LUPA_BTN = (By.CLASS_NAME, 'fa-search')


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    def getSearchInput(self):
        return self.driver.find_element(*HeaderPageLocators.SEARCH_INPUT)

    def getup(self):
        return self.driver.find_element(*HeaderPageLocators.LUPA_BTN)
