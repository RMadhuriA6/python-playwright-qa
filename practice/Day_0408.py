from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    #   Positive Testing
    page.goto("https://www.saucedemo.com/")
    #   page.wait_for_timeout(5000)
    print(page.title())
    print(page.url)
    page.get_by_role("textbox", name="Username").fill("standard_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    print(page.title())
    print(page.url)

    #   Negative testing
    page.goto("https://www.saucedemo.com/")
    print(page.title())
    print(page.url)
    page.get_by_role("textbox", name="Username").fill("locked_out_user")
    page.get_by_role("textbox", name="Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    page.wait_for_timeout(2000)

    try:
        print(page.locator('[data-test="error"]').text_content())
    except PlaywrightTimeoutError:
        print('Element not found')

    print(page.title())
    print(page.url)
    browser.close()

