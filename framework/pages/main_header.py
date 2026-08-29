from framework.pages.base_page import BasePage


class MainHeader(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.burger_menu_button = page.get_by_role("button", name="Open Menu")
