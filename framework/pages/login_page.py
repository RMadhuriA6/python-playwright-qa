class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.get_by_role("textbox", name="Username")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.invalid_Login_Msg = page.locator("[data-test='error']")