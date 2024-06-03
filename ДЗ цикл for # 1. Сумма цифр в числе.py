n = int(input("введите 3х значное число =   "))
a = n % 10
b = n % 100 // 10
c = n // 100
print("сумма цифр числа =   ", a + b + c)


k = int(input("введите число"))
print(k)
j = str(k)
sm = 0
for i in range(len(j)):
    sm+=int(j[i])
print(sm)
