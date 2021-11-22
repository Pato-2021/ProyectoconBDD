import pytest
from pytest_bdd import scenario, when, then, parsers, given
from selenium import webdriver
from Pages.HeaderPage import HeaderPage
from Pages.ProductPage import ProductPage

# constants
STORE_WEB = "https://automationteststore.com/index.php?rt=account/login"


# scenarios('../features/searchProducts.feature')
@scenario(
    "../features/searchProducts.feature",
    "Check product title",
)
def test_outlined():
    pass


@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given
@given('the search is in the header')
def open_store_web(browser):
    browser.get(STORE_WEB)
    print('the search is in the header')


@when(parsers.parse('complete "{product}"'))
def complete_product(browser, product):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(product)
    print('Complete Product')


@when('press the search button')
def click_button(browser):
    header_page = HeaderPage(browser)
    header_page.getup().click()
    print('Click in Product')


@then(parsers.parse('can check the product "{title}"'))
def check_product(browser, title):
    product_page = ProductPage(browser)
    assert product_page.getProductTitle().text == title
    print('Check Product title')
