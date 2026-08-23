from playwright.sync_api import sync_playwright
from playwright.sync_api import expect


class HerokuApp:

    def __init__(self, page):
        self.page = page
        self.url = ""

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com")


def test_alert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        alert = HerokuApp(page)
        alert.open()
        alert.page.get_by_role("link", name="JavaScript Alerts").click()
        alert.page.on("dialog", lambda dialog: print(f'Alert message: {dialog.message}'))
        alert.page.on("dialog", lambda dialog: dialog.accept())
        alert.page.get_by_role("button", name="Click for JS Alert").click()
        assert alert.page.locator('[id = "result"]').text_content() == "You successfully clicked an alert"


def test_iframes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        frame = HerokuApp(page)
        frame.open()
        frame.page.get_by_role("link", name="Frames", exact=True).click()
        frame.page.get_by_role("link", name="iFrame").click()
        page.frame_locator('[class="tox-notifications-container"]').get_by_label("Close", exact=True)


def test_MultiWindows():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        window = HerokuApp(page)
        window.open()
        window.page.get_by_role("link", name="Multiple Windows").click()
        with page.expect_popup() as popup_info:
            window.page.get_by_role("link", name="Click Here").click()
        new_page = popup_info.value
        assert new_page.get_by_role("heading", name="New Window", exact=True).is_visible()
        print(new_page.title())

