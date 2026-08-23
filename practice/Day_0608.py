from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()


    class LoginPage:
        def __init__(self):
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


    User = LoginPage()
    User.open("https://www.saucedemo.com/")
    User.login("standard_user", "secret_sauce")
    print(User.result())
    User.open("https://www.saucedemo.com/")
    User.login("locked_out_user", "secret_sauce")
    print(User.result())
    browser.close()
