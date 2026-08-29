class BurgerMenuActions:
    def __init__(self,bm_page):
        self.bm_page = bm_page

    def logout(self):
        self.bm_page.logout.click()
