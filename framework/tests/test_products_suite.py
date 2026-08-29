import pytest
from playwright.sync_api import expect
from framework.pages.login_page import LoginPage
from framework.actions.login_actions import LoginActions
from framework.pages.products_page import ProductsPage
from framework.actions.products_actions import ProductsActions
from framework.pages.main_header import MainHeader
from framework.actions.main_header_actions import MainHeaderActions

from framework.util.get_data import get_sort_data, get_login_data


@pytest.mark.parametrize("name",get_sort_data())
def test_displayed_active_option_after_sorting(page_launcher,name):
    login_page = LoginPage(page_launcher)
    login_action = LoginActions(login_page)
    login_action.login("standard_user", "secret_sauce")

    product_page = ProductsPage(page_launcher)
    product_actions = ProductsActions(product_page)
    product_actions.sorting_option(name)

    expect(product_page.active_option).to_contain_text(name)


@pytest.mark.parametrize("name", get_sort_data())
@pytest.mark.parametrize("username,password",get_login_data())
def test_item_sorting_after_sorting(page_launcher, name, username, password):
    login_page = LoginPage(page_launcher)
    login_action = LoginActions(login_page)
    login_action.login(username, password)

    product_page = ProductsPage(page_launcher)
    product_actions = ProductsActions(product_page)
    product_actions.sorting_option(name)
    raw_list, sorted_list = product_actions.item_sort(name)
    assert raw_list == sorted_list

