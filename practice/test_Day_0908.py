from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.title = ""
        self.url = ""
        self.username = ""
        self.password = ""

    def open(self, url):
        self.page.goto(url)
        self.title = self.page.title()
        self.url = self.page.url
        print(f'Login page title: {self.title}')
        print(f'Login page URL: {self.url}')

    def login(self, username, password):
        self.username = username
        self.password = password
        self.page.get_by_role("textbox", name="Username").fill(self.username)
        self.page.get_by_role("textbox", name="Password").fill(self.password)
        self.page.get_by_role("button", name="login").click()


def test_css_error_msg():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        user = LoginPage(page)
        user.open("https://www.saucedemo.com/")
        user.login("locked_out_user", "secret_sauce")
        error_msg = user.page.locator('[data-test = "error"]')
        expect(error_msg).to_be_visible()
        print(f'Login unsuccessful with {user.username} and {user.password}')
        print(f'Message displayed on screen: {error_msg.text_content()}')


def test_x_error_msg():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        user = LoginPage(page)
        user.open("https://www.saucedemo.com/")
        user.login("locked_out_user", "secret_sauce")
        error_msg = user.page.locator("//h3[@data-test='error']")
        expect(error_msg).to_be_visible()
        print(f'Login unsuccessful with {user.username} and {user.password}')
        print(f'Message displayed on screen: {error_msg.text_content()}')
