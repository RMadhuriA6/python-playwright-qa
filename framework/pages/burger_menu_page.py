from framework.pages.base_page import BasePage

class BurgerMenu(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logout = page.get_by_role("link", name="Logout")
