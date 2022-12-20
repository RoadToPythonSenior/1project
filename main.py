from interface import show_menu
from users import registration, auth

while True:

    print("Выберите действие\n")
    print("1. Регистрация")
    print("2. Авторизация\n")
    print("3. Выход\n")
    command = int(input())
    if command == 1:
        user = registration()
        if user is None:
            print("Неверные данные\n")
        show_menu(user)
    elif command == 2:
        user = auth()
        if user is None:
            print("Неверные данные\n")
        else:
            show_menu(user)
    elif command == 3:
        break
    else:
        print("Команда неизвестна\n")
