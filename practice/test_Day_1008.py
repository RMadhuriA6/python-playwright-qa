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

    def login(self, username, password):
        self.username = username
        self.password = password
        self.page.get_by_role("textbox", name="Username").fill(self.username)
        self.page.get_by_role("textbox", name="Password").fill(self.password)
        self.page.get_by_role("button", name="login").click()


def test_saucedemo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        user = LoginPage(page)
        user.open("https://www.saucedemo.com/")
        user.login("standard_user", "secret_sauce")
        user.page.keyboard.press("Enter")
        user.page.locator('[data-test="product-sort-container"]').select_option(value="lohi")
        expect(user.page.locator("//span[@data-test='active-option']")).to_contain_text("Price (low to high)")
        price_list1 = page.locator('[data-test = "inventory-item-price"]').all_text_contents()
        price_list2 = []
        for val in price_list1:
            new_val = float(val.strip('$'))
            price_list2.append(new_val)
        price_list_sorted = sorted(price_list2)
        assert price_list_sorted == price_list2
        #print(page.locator('[data-test = "inventory-item-price"]').all_inner_texts())
        print('Sorted by Price (low to high)')


def test_orange_hrm():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        user = LoginPage(page)
        user.open("https://opensource-demo.orangehrmlive.com/")
        user.login("Admin", "admin123")
        user.page.get_by_role("link", name="My Info").click()
        radio_sel = user.page.get_by_role("radio", name="Female")
        radio_sel.scroll_into_view_if_needed()
        radio_sel.evaluate("el => el.click()")
        expect(radio_sel).to_be_checked()
        print('Female selected')