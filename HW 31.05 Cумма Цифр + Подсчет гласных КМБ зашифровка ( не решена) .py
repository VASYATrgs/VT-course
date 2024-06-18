# 1. Сумма цифр в числе
# Задача: Напишите функцию, которая принимает целое число, используя цикл for, и возвращает сумму всех его цифр.
# Например, для числа 12345 функция должна вернуть 15.
#в1
n = int(input("введите 3х значное число =   "))
a = n % 10
b = n % 100 // 10
c = n // 100
print("сумма цифр числа =   ", a + b + c)

#в2
k = int(input("введите число"))
print(k)
j = str(k)
sm = 0
for i in range(len(j)):
    sm+=int(j[i])
print(sm)


# 2. Подсчет гласных букв
# Задача: Создайте функцию, которая принимает строку и возвращает количество гласных букв в этой строке.
# Используйте цикл for для перебора символов в строке. Например, для строки "Hello, world!" функция должна вернуть 3,
# так как в строке есть три гласные буквы.
#в1
name = input("введите предложение")
books = 'IOEAUioeauАЕИЫУОЕЭЮЯЙауыеэоиюяй'
s = 0
for i in name:
    if i in books:
        s = s + 1

print(s)


#в2
r = input("введите предложение с латинскими гласными")
def word(h):
    count = 0
    vowels = ('aeiouy')
    for letter in h:
        if letter in vowels:
            count += 1
    print(count)

word(r)

# 3. Игра "Камень, ножницы, бумага" с дополнительными правилами:
# Напишите программу для игры "Камень, ножницы, бумага",
# в которую могут играть два игрока.
# Каждый игрок выбирает один из трех символов.
# Камень побеждает ножницы, ножницы побеждают бумагу, бумага побеждает камень.
# В этой версии игры добавьте два дополнительных символа: "огонь" и "вода".
# Огонь побеждает камень и ножницы, но проигрывает бумаге и воде, вода побеждает камень и огонь,
# но проигрывает ножницам и бумаге.
# Программа должна принимать выбор каждого игрока и выводить результат игры.


while True: # обратите внимание на эту строку кода
    count = [0, 0]
    user_action = input("Игрок 1 Сделайте выбор — камень, ножницы или бумага: ")
    possible_actions = ["камень", "бумага", "ножницы"]
    user2_action = input("Игрок 2 Сделайте выбор — камень, ножницы или бумага: ")
    print(f'\nВы выбрали {user_action}, пользователь2 выбрал {user2_action}.\n')
    if user_action == user2_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "камень":
        if user2_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
            count[0] += 1
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
            count[1] += 1
    elif user_action == "бумага":
        if user2_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
            count[0] += 1
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
            count[1] += 1
    elif user_action == "ножницы":
        if user2_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
            count[0] += 1
        else:
            print("Камень бьет ножницы! Вы проиграли.")
            count[1] += 1
            # а также обратите внимание на код ниже
    print('счет - ', count[0],':', count[1])
    play_again = ""
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break

# 4. Зашифровка и расшифровка текста: Написать две функции - одну для зашифровки текста,
# другую для его расшифровки. Шифрование должно осуществляться путем
# сдвига каждой буквы на определенное количество позиций в алфавите.
# Например, при сдвиге на 2, буква 'a' превращается в 'c', 'b' - в 'd' и так далее.
# Функция шифрования принимает текст и число, на которое нужно сдвинуть буквы,
# а функция расшифровки - зашифрованный текст и тот же сдвиг.
# Для простоты можно считать алфавит цикличным, т.е. после 'z' снова идет 'a'.