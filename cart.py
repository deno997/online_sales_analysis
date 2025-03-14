class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Added to cart: {product.name}")

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart_items)
        print(f"Total cart value: {total}")
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("Cart items:")
            for product in self.cart_items:
                product.display_info()