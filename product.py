class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Naziv proizvoda: {self.name}")
        print(f"Cena: {self.price:.2f} ")
        print(f"Količina: {self.quantity}")

    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            print("Greška: količina ne može biti negativna!")
        else:
            self.quantity = new_quantity
            print(f"Količina proizvoda '{self.name}' ažurirana na {self.quantity}.")