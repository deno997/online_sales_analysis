from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    manager = ProductManager()

#Dodavanje proizvoda
    p1 = Product("Hleb", 80, 20)
    p2 = Product("Mleko", 120, 15)
    p3 = Product("Jaja", 15, 30)
    p4 = Product("Sir", 500, 5)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    manager.add_product(p4)

#Prikaz svih proizvoda
    manager.show_all_products()

#Prikaz ukupne vrednosti svih proizvoda
    manager.total_value()
    
cart = Cart()

    # Nasumično biramo 3 proizvoda iz ponude
random_products = random.sample(manager.products, 3)

    # Dodajemo ih u korpu
for product in random_products:
        cart.add_product(product)

    # Prikaz sadržaja korpe
cart.show_cart()

    # Ispis ukupne vrednosti korpe
total = cart.calculate_total()
print(f"\nUkupna vrednost korpe: {total:.2f}")