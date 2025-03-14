from product import Product
from product_manager import ProductManager

if __name__ == "__main__":
    manager = ProductManager()
    
    # Dodavanje proizvoda
    product1 = Product("Laptop", 1200, 3)
    product2 = Product("Phone", 800, 5)
    product3 = Product("Tablet", 500, 7)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)
    
    # Prikaz svih proizvoda
    print("Lista proizvoda:")
    manager.display_products()
    
    # Prikaz ukupne vrednosti inventara
    print("Ukupna vrednost inventara:")
    manager.total_value()
