# main.py

import sys
from user import User
from product import Product


def display_admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. Search Products")
        print("6. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            stock_quantity = int(input("Enter stock quantity: "))
            product = Product(product_id, name, category, price, stock_quantity)
            Product.add_product(product)

        elif choice == '2':
            product_id = input("Enter product ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            category = input("Enter new category (leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            stock_quantity = input("Enter new stock quantity (leave blank to keep current): ")

            try:
                Product.update_product(
                product_id,
                name=name if name else product.name,
                category=category if category else product.category,
                price=float(price) if price else product.price,
                stock_quantity=int(stock_quantity) if stock_quantity else product.stock_quantity
            )
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == '3':
            product_id = input("Enter product ID to delete: ")
            try:
                Product.delete_product(product_id)
            except ValueError:
                print("Invalid product ID. Please try again.")

        elif choice == '4':
            filter_stock = int(input("Enter minimum stock quantity to filter (leave blank for all): ") or sys.maxsize)
            Product.view_products(filter_by_stock=filter_stock)

        elif choice == '5':
            name = input("Enter product name to search (leave blank for all): ")
            category = input("Enter product category to search (leave blank for all): ")
            Product.search_products(name=name if name else None, category=category if category else None)

        elif choice == '6':
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please select again.")

def display_user_menu():
    print("\nUser Menu:")
    print("Viewing all products:")
    Product.view_products()

def main():
    while True:
        print("Welcome to Inventory Management System")
        email = input("Enter email: ")
        password = input("Enter password: ")

        user = User(email, password)
        if user.login():
            if user.role == 'admin':
                display_admin_menu()
            elif user.role == 'user':
                display_user_menu()
        else:
            print("Login failed. Please try again.")

if __name__ == "__main__":
    main()