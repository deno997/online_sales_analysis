from product import Product
from product_manager import ProductManager
from cart import Cart

if __name__ == "__main__":
    manager = ProductManager()
    
    # Dodavanje proizvoda
    product1 = Product("Laptop", 1200, 7)
    product2 = Product("Phone", 800, 9)
    product3 = Product("Tablet", 500, 4)
    
    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)