class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} (${self.price})"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_price(self):
        return sum(product.price for product in self.products)


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def checkout(self):
        print(f"{self.name} купує товари: {self.cart.products}")
        print(f"Total amount: ${self.cart.total_price()}")


p1 = Product("Ноутбук", 1000)
p2 = Product("Mouse", 50)
p3 = Product("Headpones", 120)

customer = Customer("Сергій")

customer.add_to_cart(p1)
customer.add_to_cart(p2)
customer.add_to_cart(p3)

customer.checkout()
