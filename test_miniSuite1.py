import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class WebPage:
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
        self.page.wait_for_timeout(2000)


@pytest.fixture
def page_launcher():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_login_with_valid_credentials(page_launcher):
    user = WebPage(page_launcher)
    user.open("https://www.saucedemo.com/")
    user.login("standard_user", "secret_sauce")

    assert user.page.url == "https://www.saucedemo.com/inventory.html"
    print(f'Login successful with {user.username} and {user.password}')


def test_login_with_invalid_credentials(page_launcher):
    user = WebPage(page_launcher)
    user.open("https://www.saucedemo.com/")
    user.login("locked_out_user", "secret_sauce")
    error_msg = user.page.locator('[data-test = "error"]')
    expect(error_msg).to_be_visible()
    print(f'Login unsuccessful with {user.username} and {user.password}')
    print(f'Message displayed on screen: {error_msg.text_content()}')


def test_saucedemo_price_sorting_lo_to_hi(page_launcher):
    user = WebPage(page_launcher)
    user.open("https://www.saucedemo.com/")
    user.login("standard_user", "secret_sauce")
    user.page.keyboard.press("Enter")
    user.page.locator('[data-test="product-sort-container"]').select_option(value="lohi")
    expect(user.page.locator("//span[@data-test='active-option']")).to_contain_text("Price (low to high)")
    price_list1 = user.page.locator('[data-test = "inventory-item-price"]').all_inner_texts()
    price_list2 = []
    for val in price_list1:
        new_val = float(val.strip('$'))
        price_list2.append(new_val)
    price_list_sorted = sorted(price_list2)
    assert price_list_sorted == price_list2
    print('Sorted by Price (low to high)')


def test_alert_accept(page_launcher):
    alert = WebPage(page_launcher)
    alert.open("https://the-internet.herokuapp.com")
    alert.page.get_by_role("link", name="JavaScript Alerts").click()
    alert.page.on("dialog", lambda dialog: print(f'Alert message: {dialog.message}'))
    alert.page.on("dialog", lambda dialog: dialog.accept())
    alert.page.get_by_role("button", name="Click for JS Alert").click()
    assert alert.page.locator('[id = "result"]').text_content() == "You successfully clicked an alert"


def test_iframes_static(page_launcher):
    frame1 = WebPage(page_launcher)
    frame1.open("https://the-internet.herokuapp.com")
    frame1.page.get_by_role("link", name="Frames", exact=True).click()
    frame1.page.get_by_role("link", name="iFrame").click()
#   iframe_text = frame.page.frame_locator("//iframe[@title='Rich Text Area']").locator("body").text_content()
    iframe_text = frame1.page.locator("//iframe[@title='Rich Text Area']").content_frame.locator("body").text_content()
    assert iframe_text == "Your content goes here."


def test_iframes_editing(page_launcher):
    frame2 = WebPage(page_launcher)
    frame2.open("https://practice.expandtesting.com/iframe")
    innerFrame = frame2.page.locator("//iframe[@id='email-subscribe']").content_frame
    innerFrame.locator("//input[@id='email']").fill("abc@test.com")
    innerFrame.get_by_role("button", name="Subscribe").click()
    assert innerFrame.locator("//div[@id='success-message']").text_content() == "You are now subscribed!"


def test_multiple_tabs(page_launcher):
    window = WebPage(page_launcher)
    window.open("https://the-internet.herokuapp.com")
    window.page.get_by_role("link", name="Multiple Windows").click()
    with page_launcher.expect_popup() as popup_info:
        window.page.get_by_role("link", name="Click Here").click()
    new_page = popup_info.value
    assert new_page.get_by_role("heading", name="New Window", exact=True).is_visible()
    print(new_page.title())


def test_orangeHRM_gender_radio_button(page_launcher):
    user = WebPage(page_launcher)
    user.open("https://opensource-demo.orangehrmlive.com/")
    user.login("Admin", "admin123")
    user.page.get_by_role("link", name="My Info").click()
    radio_sel = user.page.get_by_role("radio", name="Female")
    radio_sel.scroll_into_view_if_needed()
    radio_sel.evaluate("el => el.click()")
    expect(radio_sel).to_be_checked()
    print('Female selected')
