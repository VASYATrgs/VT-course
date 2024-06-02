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