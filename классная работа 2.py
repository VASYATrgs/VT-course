# ЦИКЛ ФОР
n = 1
word = "python"
for letter in word:
     print(f"буква номре {n}: {letter}")
     n += 1

word1 = "pythin"

for x in range(1, 100, 10):
       print(word1[x])


list_example = [string_example, int_example, float_example, 1, "test_string", False]
# добавление
my_list =[]#
my_list.append(1)
my_list.append("str")
my_list.append(True)

# получение
print(my_list[1])

for g in list_example:
    print(g)


k = int(input())
my_list = []
s = 0
while s < k:
    number = int(input())
    my_list.append(number)
    s += 1

my_list.sort()
print(my_list)

for i in range(k):
     number = int(input())
     my_list.append(number)

my_list.sort()
print(my_list)


