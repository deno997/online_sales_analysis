from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Proizvod '{product.name}' je uspešno dodat.")

    def show_all_products(self):
        if not self.products:
            print("Nema dostupnih proizvoda.")
        else:
            print("\n--- Lista svih proizvoda ---")
            for product in self.products:
                product.show_info()
                print("----------------------------")

    def total_value(self):
        total = sum(p.price * p.quantity for p in self.products)
        print(f"Ukupna vrednost svih proizvoda: {total:.2f}")
        return total
    
    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Proizvod '{name}' je uklonjen.")
                return
        print(f"Proizvod '{name}' nije pronađen.")