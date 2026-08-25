from framework.pages.login_page import LoginPage
from framework.pages.products_page import ProductsPage
from framework.actions.login_actions import LoginActions
from framework.actions.products_actions import ProductsActions
from playwright.sync_api import expect


def test_sample1(page_launcher):
    login_page = LoginPage(page_launcher)
    valid_login = LoginActions(login_page)

    valid_login.login("standard_user", "secret_sauce")
    assert valid_login.login_page.page.url == "https://www.saucedemo.com/inventory.html"


def test_sample2(page_launcher):
    login_page = LoginPage(page_launcher)
    valid_login = LoginActions(login_page)
    valid_login.login("standard_user", "secret_sauce")
    product1 = ProductsPage(page_launcher)
    product_action1 = ProductsActions(product1)
#   product_action1.product1.valid_login.login("standard_user", "secret_sauce")
    print(product_action1.product1.page.url)
#   expect(product_action1.product1.title_locator).to_have_text("Products")
    product_action1.sorting_z_a()
    product_action1.check_sorting_z_a()
    assert product_action1.sort_list == product_action1.sorted_list





