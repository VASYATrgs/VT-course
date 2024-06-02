print("факториал числа")  #3 факториал числа

n = int(input("введите число: "))

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)