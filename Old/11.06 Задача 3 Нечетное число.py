data = []
n = int(input())
for i in range(n):
    new_elem = int(input())
    data.append(new_elem)

print(min([elem for elem in data if elem % 2 != 0]))