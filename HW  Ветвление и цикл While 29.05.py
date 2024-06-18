# 1. Классификатор возраста: Написать программу, которая принимает возраст пользователя и выводит категорию:
# "ребенок" (0-12), "подросток" (13-17), "взрослый" (18-64) или "пожилой человек" (65 и старше).

age = int(input('Введите возраст:'))
if 0 < age <= 12:
    print(age, 'ребенок!')
if 13 <= age <= 17:
    print(age, 'подросток!')
if 18 <= age <= 64:
    print(age, 'взрослый!')
if age > 64:
    print(age, 'пожилой!')

# 3. Программа для оценки пароля: Написать программу, которая анализирует введенный пароль и выводит его оценку:
# слабый (менее 6 символов), средний (6-12 символов, содержит только буквы и цифры)
# или сильный (более 12 символов, содержит буквы, цифры и спецсимволы).

#в 1 простой
str = input("Придумайте пароль (не менее 6 символов. Пароль должен состоять из цифр и латинских букв):")
print(len(str))
c=(len(str))
print(c)
if 0 < c <= 6:
    print(c, 'слабый!')
if 6 < c <= 12:
    print(c, 'средний!')
if 12 < c :
    print(c, 'сильный!')

# в 2

password = input("Придумайте пароль (не менее 6 символов. Пароль должен состоять из цифр и латинских букв):")
length = len(password)
contains_letters = any(char.isalpha() for char in password)
# isalpha() - вхождение в строку букв
contains_digits = any(char.isdigit() for char in password)
#isdigit() - вхождение в строку цифр
contains_specials = any(not char.isalnum() for char in password)
#isalnum() - вхождение в строку букв и цифр:

if length < 6:
    reliability = "пароль слабый"
elif 6 <= length <= 12:
    if contains_letters and contains_digits and not contains_specials:
        strength = "пароль средний"
    else:
        strength = "пароль слабый"
elif length >= 12:
    if contains_letters and contains_digits and contains_specials:
        strength = "пароль сильный!"
    else:
        strength = "пароль средний"


print(f"Оценка вашего пароля: {strength}")


# 4. Определение високосного года: Написать программу, которая определяет, является ли год,
# введенный пользователем, високосным. Год считается високосным, если он делится на 4,
# но если он делится на 100, он не является високосным, за исключением случаев, когда он делится на 400.

year = int(input("введите год: "))
if( (year % 4) == 0):
    if ( (year % 100 ) == 0):

        if ( (year % 400) == 0):

            print("{0} высокосный год".format(year))
        else:

            print("{0} невысокосный".format(year))
    else:

        print("{0} высокосный".format(year))

else:

    print("{0} невысокосный".format(year))

#     Цикл while

# 1. Подсчет суммы чисел:
# Напишите программу, которая считает сумму чисел от 1 до N, где N задается пользователем.

# простое или сложное число
n = int(input("введите число: "))
flag = False
i = 2
while i < n:
    if n % i ==0:
        flag = True
        print(f'{n} делится на {i}')
    i += 1
if flag:
    print(f'Таким образом, {n} не является простым числом')
else:
    print(f'{n} - простое число')


# 2. Поиск суммы 2:
# Напишите программу, которая запрашивает у пользователя числа до тех пор,
# пока не будет введен 0, и находит сумму из введенных чисел.

while True:
  output = ""
  num = int(input("введите число: "))

  if num == 0:
    exit()

  for i in range(1, num+1):
    output += "{}".format(i)
    if i != num:
      output += "+"
  output += " = {}".format(sum(range(num+1)))
  print (output)