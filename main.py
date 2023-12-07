# main.py
from product_repository import ProductRepository
from shopping_cart import ShoppingCart
from checkout import Checkout

def main():
    product_repository = ProductRepository()
    products = product_repository.get_products()

    shopping_cart = ShoppingCart()
    for product in products:
        shopping_cart.add_to_cart(product)

    shopping_cart.display_cart()

    checkout = Checkout()
    checkout.process_checkout(shopping_cart)

if __name__ == "__main__":
    main()
