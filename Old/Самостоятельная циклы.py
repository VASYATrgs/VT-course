i = 1999
while i > 100:
    print(i)
    i /=2

for j in "hello wordl":
    if j == 'w':
        continue  # пропустить w
    print(j * 2, end = "" )

for c in "hello wordl":
    if c == 'k':
        break #выход из цикла
    print(c * 2, end = "" )
else:
    print("Буквы а нет в слове")