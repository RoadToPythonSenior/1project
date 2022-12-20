from users import Customer, Seller
from products import products_in_stock, Book, Phone


def show_customer_menu(customer):
    print("1. Пополнить баланс")
    print("2. Перейти в каталог")
    command = int(input())
    if command == 1:
        print("Введите количество денег")
        amount = float(input())
        customer.add_money(amount)
    elif command == 2:
        print("Выберите товар")
        idx = 1
        for product in products_in_stock:
            print(f"{idx}. {product.name}")
        product_number = int(input())
        if product_number < len(products_in_stock):
            product = products_in_stock[product_number-1]
        else:
            print("Неверный товар")
            return
        customer.buy(product)


def show_seller_menu(seller):
    while True:
        print("1. Добавить товар")
        print("2. Показать текущий баланс")
        print("3. Выйти в главное меню")
        command = int(input())
        if command == 1:
            print("Выберите тип продукта")
            print("1. Книги")
            print("2. Телефоны")
            type_command = int(input())
            print("Введите название товара")
            product_name = input()
            print("Введите цену за товар")
            price = float(input())
            count = int(input("Введите количество"))
            if type_command == 1:
                author = input("Введите имя автора")
                product = Book(author, price, count, seller, product_name)
            elif type_command == 2:
                model = input("Введите модель")
                product = Phone(model, price, count, seller, product_name)
            else:
                print("Неизвестный тип товара")
                return
            products_in_stock.append(product)
        if command == 2:
            print(f"Текущий баланс {seller.balance}")
        if command == 3:
            break


def show_menu(user):
    if type(user) == Customer:
        show_customer_menu(user)
    elif type(user) == Seller:
        show_seller_menu(user)

