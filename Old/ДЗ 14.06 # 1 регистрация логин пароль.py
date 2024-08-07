import os
print(os.environ)

login = ''
password = ''

print("Добро пожаловать в меню")
while True:
    print("Чтобы зарегистрироваться нажмите 1, чтобы войти в существующий аккаунт нажмите 2")
    print()
    menu = int(input())  # переменная выбора регестрации или входа

    if menu == 1:
        print()
        os.system("cls")
        login = input('Придумайте логин: ')
        password = input('Придумайте пароль: ')
        print()
        os.system("cls")
        print("Вы успешно зарегестрировались!")
        os.system("cls")
        print()
    if menu == 2:
        print()
        os.system("cls")
        log = input('Введите логин: ')
        pas = input('введите пароль: ')
        if log == login and pas == password:  # если символы переменной log равны символам переменной login, и
            print()  # если символы переменной pas равны символам переменной password, то
            os.system("cls")  # происходит вход
            print('вы успешно вошли в аккаунт!')
            while True:
                print("чтобы выйти нажмите 3, чтобы изменить УЗ 4")
                print()
                menu = int(input())  # переменная выбора выхода или изменения регистрации
                if menu == 3:
                    print("выход")
                    break
                if menu == 4:
                    print("Введите новый логи и пароль")
        elif log == login or pas == password:  # если какая-то одна переменная равна другой переменной, например log == login,
            os.system("cls")  # тогда вход не производится, т.к. не правильный логин или пароль
            print('Неправильный логин или пароль!')
            print()
        else:
            os.system("cls")  # если не совпадают ни одни данные, то
            print('Аккаунта не существует!')  # вход не производится, т.к. этих данных не существует
            print()
