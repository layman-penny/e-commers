# product_repository.py
from product import Product

class ProductRepository:
    def __init__(self):
        self.products = [
            Product(1, 'Product A', 19.99),
            Product(2, 'Product B', 29.99),
            Product(3, 'Product C', 39.99),
            # Add more products as needed
        ]

    def get_products(self):
        return self.products
