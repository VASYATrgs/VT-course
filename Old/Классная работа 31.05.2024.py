
from random import randint

x = randint(1, 100)
attempt = 0

while True:
    print("Я загадал число от 1 до 100, угадай его :)")
    user_num = int(input("Ваша попытка: "))
    attempt += 1
    if user_num == x:
        print(f"Ты угадал число, молодец!\nКоличество твоих попыток: {attempt}\nСпасибо за игру!")
        break
    elif user_num > x:
        print("Моё число меньше.")
    elif user_num < x:
        print("Моё число больше")



    d = int(input("введите число\n"))
    print(d)

    x = 15
    while d !=x:
        d = int(input("введите число\n"))
        if d < x:
            print("введенное число меньше загаданного")
        if d > x:
            print("введенное число больше загаданного")
    print("вы угадали")

    print("игра угадай число")
    print("угадай число от 1 до 100")
    d = int(input("введите число\n"))
    print(d)
    e = 1
    x = 15
    while d != x:
        e += 1
        d = int(input("введите число\n"))
        if d < x:
            print("введенное число меньше загаданного")
        if d > x:
            print("введенное число больше загаданного")
    print(f"вы угадали с {e} попытки")
