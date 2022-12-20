from products import products_in_stock

users = {}


class User:
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._balance = 0

    def get_login(self):
        return self._login

    def get_password(self):
        return self._password

    def add_money(self, amount):
        if self._balance + amount < 0:
            raise Exception("В результате операции баланс станет меньше нуля")
        self._balance += amount


class Seller(User):
    pass


class Customer(User):
    def buy(self, product):
        self.add_money(-product.get_price())
        product.get_seller().add_money(product.get_price())
        products_in_stock.remove(product)
        print(f"Продукт {product.name} успешно был куплен у продавца {product.get_seller().get_login()})")


def auth():
    login = input("Введите логин\n")
    password = input("Введите пароль\n")
    if login not in users or users[login].get_password() != password:
        return None
    return users[login]


def registration():
    login = input("Введите новый логин\n")
    if login in users:
        print("Такой пользователь уже существует")
        return None
    password = input("Введите новый пароль\n")
    print("Выберете тип аккаунта")
    print("1. Продавец")
    print("2. Покупатель")
    command = int(input())
    if command == 1:
        user = Seller(login, password)
    elif command == 2:
        user = Customer(login, password)
    else:
        print("Неизвестная команда")
        return None
    users[login] = user
    return user
