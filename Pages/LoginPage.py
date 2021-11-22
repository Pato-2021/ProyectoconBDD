from selenium.webdriver.common.by import By

class LoginPageLocators:
    USER_INPUT = (By.ID, 'loginFrm_loginname')
    PASS_INPUT = (By.ID, 'loginFrm_password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[title="Login"]')
    ERROR = (By.CSS_SELECTOR, 'div.alert.alert-error.alert-danger')

class LoginPage:

    # siempre tiene que estar este constructor
    def __init__(self, driver):
        self.driver = driver

    def getUserInput(self):
        return self.driver.find_element(*LoginPageLocators.USER_INPUT)

    def getPassInput(self):
        return self.driver.find_element(*LoginPageLocators.PASS_INPUT)

    def getLoginBtn(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BTN)

    def getErrorMessage(self):
        return self.driver.find_element(*LoginPageLocators.ERROR)