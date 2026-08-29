class ProductsActions:
    def __init__(self, product_action):
        self.names = []
        self.prices = []
        self.sorted_names = []
        self.sorted_prices = []
        self.product_action = product_action

    def sorting_option(self, name):
        self.product_action.sort_container.select_option(label=name)

    def item_sort(self, name):
        if name in ['Name (A to Z)', 'Name (Z to A)']:
            self.names = self.product_action.item_name.all_inner_texts()
            if name == 'Name (A to Z)':
                self.sorted_names = sorted(self.names)
            elif name == 'Name (Z to A)':
                self.sorted_names = sorted(self.names, reverse=True)
            return self.names, self.sorted_names
        elif name in ['Price (low to high)', 'Price (high to low)']:
            price_text = self.product_action.item_price.all_inner_texts()
            for val in price_text:
                new_val = float(val.strip('$'))
                self.prices.append(new_val)
            if name == 'Price (low to high)':
                self.sorted_prices = sorted(self.prices)
            elif name == 'Price (high to low)':
                self.sorted_prices = sorted(self.prices, reverse=True)
            return self.prices, self.sorted_prices
