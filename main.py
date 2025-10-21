from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

#Dodavanje proizvoda
    p1 = Product("Hleb", 80, 40)
    p2 = Product("Mleko", 120, 25)
    p3 = Product("Jaja", 15, 35)
    p4 = Product("Sir", 500, 8)

    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)
    manager.add_product(p4)
    
if __name__ == "__main__":
    main()