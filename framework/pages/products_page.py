from framework.pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title_locator = page.locator("[data-test='title']")
        self.sort_container = page.locator("[class='product_sort_container']")
        self.item_name = page.locator("[data-test='inventory-item-name']")
        self.item_price = page.locator("[data-test ='inventory-item-price']")
        self.active_option = page.locator("//span[@data-test='active-option']")


