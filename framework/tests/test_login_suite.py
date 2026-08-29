import pytest
from playwright.sync_api import expect
from framework.pages.login_page import LoginPage
from framework.actions.login_actions import LoginActions
from framework.pages.burger_menu_page import BurgerMenu
from framework.actions.burger_menu_actions import BurgerMenuActions
from framework.pages.main_header import MainHeader
from framework.actions.main_header_actions import MainHeaderActions

from framework.util.get_data import get_login_data_for_login


@pytest.mark.parametrize("username,password,scenario",get_login_data_for_login())
def test_login_suite(page_launcher, username, password, scenario):
    login_page = LoginPage(page_launcher)
    login_action = LoginActions(login_page)

    login_action.login(username,password)

    if scenario == 'Locked out user':
        expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    elif scenario in ['Empty username with valid password', 'Both fields Empty']:
        expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: Username is required")
    elif scenario == 'Valid username with Empty password':
        expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: Password is required")
    elif scenario in ['white-spacing check','Case-sensitivity check','Invalid username with valid password',
                      'Valid username with invalid password', 'Invalid username with invalid password']:
        expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: "
                                                          "Username and password do not match any user in this service")
    else:
        expect(page_launcher).to_have_url("https://www.saucedemo.com/inventory.html")


def test_sql_injection(page_launcher):
    login_page = LoginPage(page_launcher)
    login_action = LoginActions(login_page)

    login_action.login("' OR '1'='1", "secret_sauce")
    expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: "
                                                      "Username and password do not match any user in this service")


def test_login_back(page_launcher):
    login_page = LoginPage(page_launcher)
    login_actions = LoginActions(login_page)
    login_actions.login("standard_user", "secret_sauce")

    main_header = MainHeader(page_launcher)
    main_header_actions = MainHeaderActions(main_header)
    main_header_actions.open_menu()

    bm_page = BurgerMenu(page_launcher)
    bm_actions = BurgerMenuActions(bm_page)
    bm_actions.logout()

    page_launcher.go_back()
    expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: "
                                                      "You can only access '/inventory.html' when you are logged in.")


