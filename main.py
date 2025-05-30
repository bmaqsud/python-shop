from product import show_product_list
from cart import (
    add_cart,
    show_cart,
    remove_product,
    show_check

)


products = [
    {"id": 1, "name": "Apple iPhone 14", "price": 999.99, "stock": 10},
    {"id": 2, "name": "Samsung Galaxy S23", "price": 899.99, "stock": 15},
    {"id": 3, "name": "Google Pixel 7", "price": 799.99, "stock": 8},
    {"id": 4, "name": "MacBook Pro 14", "price": 1999.99, "stock": 5},
    {"id": 5, "name": "Dell XPS 13", "price": 1299.99, "stock": 7},
    {"id": 6, "name": "Sony WH-1000XM5", "price": 349.99, "stock": 20},
    {"id": 7, "name": "Apple Watch Series 8", "price": 399.99, "stock": 12},
    {"id": 8, "name": "iPad Pro 11", "price": 899.99, "stock": 6},
    {"id": 9, "name": "Logitech MX Master 3", "price": 99.99, "stock": 25},
    {"id": 10, "name": "Samsung 27\" Monitor", "price": 249.99, "stock": 10}
]
cart = []

def show_menu():
    print()
    print("--------Menu-------")
    print("1. Mahsulotlarni ko'rish")
    print("2. Mahsulotni savatchaga qo'shish")
    print("3. Savatchani ko'rish")
    print("4. Mahsulotni savatchadan olib tashlash")
    print("5. Checkni olish")

def main():
    while True:
        show_menu()

        choice = input("Menu tanlang: ")

        if choice == "1":
            show_product_list(products)
        elif choice == "2":
            show_product_list(products)
            add_cart(cart)
        elif choice == "3":
            show_cart(cart, products)
        elif choice == "4":
            remove_product(cart, products)
        elif choice == "5":
            show_check(cart, products)
        else:
            print("xato menu!")

main()
