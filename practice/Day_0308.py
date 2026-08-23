from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://swaglabs.in/")
    page.wait_for_timeout(5000)
    print(page.title())

    page.mouse.wheel(0, 2100)
    page.wait_for_timeout(5000)
    eLocator = page.get_by_role("link", name="Preset Pack 2")
    count = eLocator.count()
    print(f"Matching elements found after scroll: {count}")
    eLocator.click()
    page.wait_for_timeout(5000)
    print(page.url)
    print(page.title())

    browser.close()
