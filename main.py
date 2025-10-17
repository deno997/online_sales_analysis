from product import Product
from product_manager import ProductManager

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

if __name__ == "__main__":
    main()