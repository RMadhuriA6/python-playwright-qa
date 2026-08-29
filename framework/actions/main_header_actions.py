

class MainHeaderActions:
    def __init__(self, header_page):
        self.header_page = header_page

    def open_menu(self):
        self.header_page.burger_menu_button.click()
