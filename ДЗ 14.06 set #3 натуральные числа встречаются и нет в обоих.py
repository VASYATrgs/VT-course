n = int(input("введите число натуральных чисел"))
r1 = list(map(int, input("введите последовательность чисел 1").split(' ')))
r2 = list(map(int, input("введите последовательность чисел 2").split(' ')))

a1 = []
a2 = []

for i in range(1, n + 1):
    if (i in r1) & (i in r2):
        a1 += [i]
    if (not (i in r1)) & (not (i in r2)):
        a2 += [i]

for i in a1:
    print(i, end=' ')
print()
for i in a2:
    print(i, end=' ')