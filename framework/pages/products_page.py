class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.title_locator = page.locator("[data-test='title']")
        self.sortZ2A = page.locator("[class='product_sort_container']")
        self.item_name = page.locator("[data-test='inventory-item-name']")


