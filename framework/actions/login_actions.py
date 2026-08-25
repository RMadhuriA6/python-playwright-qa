

class LoginActions:
    def __init__(self, login_page):
        self.url = None
        self.login_page = login_page

    def login(self, username, password):
        self.login_page.page.goto("https://www.saucedemo.com/")
        self.login_page.username_field.fill(username)
        self.login_page.password_field.fill(password)
        self.login_page.login_button.click()
