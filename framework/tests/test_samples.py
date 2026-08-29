from framework.actions.products_actions import ProductsActions
from framework.pages.login_page import LoginPage
from framework.actions.login_actions import LoginActions
from framework.pages.burger_menu_page import BurgerMenu
from framework.actions.burger_menu_actions import BurgerMenuActions
from framework.pages.main_header import MainHeader
from framework.actions.main_header_actions import MainHeaderActions
from playwright.sync_api import expect

from framework.pages.products_page import ProductsPage


def test_item_sorting_after_sorting(page_launcher):
    login_page = LoginPage(page_launcher)
    login_action = LoginActions(login_page)
    login_action.login("standard_user", "secret_sauce")

    product_page = ProductsPage(page_launcher)
    product_actions = ProductsActions(product_page)
    product_actions.sorting_option('Price (high to low)')

    raw_list, sorted_list = product_actions.item_sort("Price (high to low)")
    print(raw_list)
    print(sorted_list)
    assert raw_list == sorted_list



