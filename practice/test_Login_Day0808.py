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
        self.page.wait_for_timeout(2000)

    def result(self):
        if self.page.url == "https://www.saucedemo.com/inventory.html":
            return f'Login successful with {self.username} and {self.password}'
        else:
            return f'Login unsuccessful with {self.username} and {self.password}'


def test_validuser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        user = LoginPage(page)
        user.open("https://www.saucedemo.com/")
        user.login("standard_user", "secret_sauce")

        assert user.page.url == "https://www.saucedemo.com/inventory.html"
        print(f'Login successful with {user.username} and {user.password}')


def test_invaliduser():
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

