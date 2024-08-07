print('Программа нахождения количества положительных чисел')
data = []
n = int(input())
for i in range(n):
    new_elem = int(input())
    data.append(new_elem)
print(data)


count = 0
for i in data:
     if i > 0:
         count +=1
print (count)

