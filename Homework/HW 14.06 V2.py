base = {}

print("Добро пожаловать в приложение")


def password_check(login, password):
    return True if password == base[login] else False


while True:
    choice = input(
        "Введите 1, чтобы зарегистрироваться \nВведите 2, чтобы авторизоваться \nВведите 3, чтобы выйти из программы "
        "\nВведите 4, чтобы сменить пароль пользователя\nВведите 5, чтобы просмотреть словарь \n")
    print(base)

    if choice == "1":
        print("Процесс регистрации")
        login = input("Введите логин: \n")
        if login in base:
            print("Такой логин занят")
            continue

        password = input("Введите пароль: \n")
        if password == "":
            print("Строка пароля не может быть пустой")
            continue

        password_repeat = input("Введите пароль повторно: \n")
        if password == password_repeat:
            base[login] = password
            print("Процесс регистрации завершён")
            print(base)
        elif password != password_repeat:
            print("Пароли не совпадают")
            continue
        else:
            print("Ошибка")
            break

    elif choice == "2":
        print("Процесс авторизации")
        login = input("Введите логин: \n")
        count = 0
        if login in base:
            password = input("Введите пароль: \n")
            if password_check(login, password):
                print("Вы успешно вошли в систему")
                print(base)
                break
            while count < 2:
                count += 1
                print("Пароль неверный")
                print("Попробуйте ещё раз")
                password = input("Введите пароль: \n")
                if password_check(login, password):
                    print("Вы успешно вошли в систему")
                    print(base)
                    break
            print("Пароль неверный")
            print("Пройдите авторизацию заново")
            break
        else:
            print("Такой пользователь не зарегистрирован")
            continue

    elif choice == "4":
        print("Смена пароля")
        login = input("Введите ваш логин: \n")
        if login in base:
            password = input("Введите ваш пароль: \n")
            if password_check(login, password):
                print(base)
                print("Смена пароля")
                print("Введите ваш новый пароль")
                new_password = input()
                base[login] = new_password
                print(base)
                continue
            else:
                print("Пароль неверный")
                continue
        else:
            print("Логин не найден")
            continue
    elif choice == "5":
        print("данные о паролях")
        login = input("Введите ваш логин admin: \n")
        if login in base:
            password = input("Введите ваш пароль: \n")
            if password_check(login, password):
                for login, password in base.items():
                    print(login)
                    print(password)
                    print(password)
                continue
            else:
                print("Пароль неверный")
                continue
        else:
            print("Логин не найден")
            continue
    else:
        print("Выход из программы")
        break
