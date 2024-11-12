# product.py

class Product:
    product_list = []
    low_stock_threshold = 10

    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    @classmethod
    def add_product(cls, product):
        cls.product_list.append(product)
        print("Product added successfully.")

    @classmethod
    def update_product(cls, product_id, **kwargs):
        for product in cls.product_list:
            if product.product_id == product_id:
                product.name = kwargs.get('name', product.name)
                product.category = kwargs.get('category', product.category)
                product.price = kwargs.get('price', product.price)
                product.stock_quantity = kwargs.get('stock_quantity', product.stock_quantity)
                print("Product updated successfully.")
                return
        print("Product not found.")

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.product_list:
            if product.product_id == product_id:
                cls.product_list.remove(product)
                print("Product deleted successfully.")
                return
        print("Product not found.")

    @classmethod
    def view_products(cls, filter_by_stock=None):
        if cls.product_list:
            for product in cls.product_list:
                if filter_by_stock is None or product.stock_quantity <= filter_by_stock:
                    print(f"ID: {product.product_id}, Name: {product.name}, "
                          f"Category: {product.category}, Price: {product.price}, "
                          f"Stock: {product.stock_quantity}")
                    if product.stock_quantity <= cls.low_stock_threshold:
                        print(f"Low stock alert for {product.name}!")
        else:
            print("No products in the inventory.")

    @classmethod
    def search_products(cls, name=None, category=None):
        matching_products = cls.product_list[:]
        if name:
            matching_products = [p for p in matching_products if name.lower() in p.name.lower()]
        if category:
            matching_products = [p for p in matching_products if category.lower() in p.category.lower()]

        if matching_products:
            for product in matching_products:
                print(f"ID: {product.product_id}, Name: {product.name}, "
                      f"Category: {product.category}, Price: {product.price}, "
                      f"Stock: {product.stock_quantity}")
        else:
            print("No matching products found.")