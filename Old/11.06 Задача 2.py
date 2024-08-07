data = []
n = int(input())
for i in range(n):
    new_elem = int(input())
    data.append(new_elem)
print(len([elem for elem in data if elem > 0]))

print(data)
minimum = 1_000_000
for elem in data:
    if elem > 0 and (minimum is None or elem < minimum):
        minimum = elem

print(minimum)


print(min([elem for elem in data if elem > 0]))