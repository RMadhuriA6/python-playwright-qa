import pytest
from playwright.sync_api import expect
from framework.pages.login_page import LoginPage
from framework.actions.login_actions import LoginActions

from framework.util.get_login_data import get_login_data


@pytest.mark.parametrize("username,password,scenario",get_login_data())
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
    elif scenario in ['Invalid username with valid password', 'Valid username with invalid password', 'Invalid username with invalid password']:
        expect(login_page.invalid_Login_Msg).to_have_text("Epic sadface: Username and password do not match any user in this service")
    else:
        expect(page_launcher).to_have_url("https://www.saucedemo.com/inventory.html")
