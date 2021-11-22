import pytest
from pytest_bdd import scenarios, when, then, parsers, given
from selenium import webdriver
from Pages.LoginPage import *
from Pages.AccountPage import AccountPage

# constants
STORE_WEB = "https://automationteststore.com/index.php?rt=account/login"


scenarios('../features/login.feature')

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given
@given('the Store webPage')
def open_store_web(browser):
    browser.get(STORE_WEB)
    print('Open Login Store WebPage')


@when(parsers.parse('complete "{username}" and "{password}"'))
def complete_user_pass(browser, username, password):
    login_page = LoginPage(browser)
    login_page.getUserInput().send_keys(username)
    login_page.getPassInput().send_keys(password)
    login_page.getLoginBtn().click()
    print('Step: complete user y pass')


@then('my account page is displayed')
def check_account(browser):
    account_page = AccountPage(browser)

    assert account_page.getTitle().text == 'MY ACCOUNT Patricia'
    print("Account page is displayed")


@then(parsers.parse('the error "{error_message}" is displayed'))
def error_login(browser, error_message):
    login_page = LoginPage(browser)

    assert error_message in login_page.getErrorMessage().text
    print('The error is: ' + error_message)
