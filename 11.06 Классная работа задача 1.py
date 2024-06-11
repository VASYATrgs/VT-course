from array import array

A = array("i")
N = int(input('Введите число N(чтсдл элементов) = '))
A = [0] * N
for i in range(0, N):
    print('A[', i, ']=', end=" ");
    A[i] = int(input())
S = Sum = 0
for i in range(0, N):
    Sum += A[i]
    if A[i] > 0:
        S += 1

print('количество положительных элементов = ', S)
print("Сумма", Sum)
