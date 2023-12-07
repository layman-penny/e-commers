# shopping_cart.py
from product import Product

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def display_cart(self):
        print("Shopping Cart:")
        for product in self.products:
            print(f"Product: {product.name} - Price: {product.price}")
