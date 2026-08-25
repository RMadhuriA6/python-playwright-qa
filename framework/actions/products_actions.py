class ProductsActions:
    def __init__(self, product1):
        self.sort_list = None
        self.sorted_list = None
        self.product1 = product1

    def sorting_z_a(self):
        self.product1.sortZ2A.select_option("Name (Z to A)")

    def check_sorting_z_a(self):
        self.sort_list = self.product1.item_name.all_inner_texts()
        self.sorted_list = sorted(self.sort_list, reverse=True)