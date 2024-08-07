age = int(input('Введите возраст:'))
if 0 < age <= 12:
    print(age, 'ребенок!')
if 13 <= age <= 17:
    print(age, 'подросток!')
if 18 <= age <= 64:
    print(age, 'взрослый!')
if age > 64:
    print(age, 'пожилой!')


str = "password"
print(len(str))
c=(len(str))
print(c)
if 0 < c <= 6:
    print(c, 'слабый!')
if 6 < c <= 12:
    print(c, 'средний!')
if 12 < c :
    print(c, 'сильный!')

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


import math
a = int(input("Введите значение a= "))
b = int(input("Введите значение b= "))
j = int(input("Введите значение j= "))
D = b ** 2 - 4 * a * j
print(D)
if D < 0:
  print("Корней нет")
elif D == 0:
  x = -b / 2 * a
  print (x)
else:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 * a)
  print(x1)
  print(x2)