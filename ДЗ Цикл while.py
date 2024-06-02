#1 найти сумму всех чисел до n
n = int(input("введите количество чисел которые вы хотите сложить: "))
sum = 0
for i in range(n):
    x = int(input("введите число: "))
    sum += x

print(sum)



