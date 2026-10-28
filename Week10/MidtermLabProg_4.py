class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


    def __str__(self):
        return (f"Product: {self.product_name}\n"
                f"Price: PHP {self.price:.2f}")




class ElectronicProduct(Product):
    def __init__(self, product_name, price, warranty_months):
        super().__init__(product_name, price)
        self.warranty_months = warranty_months


    def __str__(self):
        return (f"{super().__str__()}\n"
                f"Warranty: {self.warranty_months} months")




class Laptop(ElectronicProduct):
    def __init__(self, product_name, price, warranty_months, ram_gb, storage_gb):
        super().__init__(product_name, price, warranty_months)
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb


    def __str__(self):
        return (f"{super().__str__()}\n"
                f"RAM: {self.ram_gb} GB\n"
                f"Storage: {self.storage_gb} GB")




def main():
    laptops = [
        Laptop("Lenovo Laptop", 35000.00, 24, 16, 512),
        Laptop("MacBook Pro", 75000.00, 12, 32, 1024)
    ]

    for laptop in laptops:
        print(laptop)
        print()

    




if __name__ == "__main__":
    main()