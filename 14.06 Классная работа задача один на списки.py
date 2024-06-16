string = input('Введите текст: ').lower().split()
for i, word in enumerate(set(string), 1):
    print(f'{i}. {word} {string.count(word)} раз.')

name = ['Маша','Вася','Петя']
age = [7,40,94]
name_and_age = dict(zip(name, age))
print(name_and_age)



list1 = ["Маша", "Вася", "Петя", "Коля"]
list2 = [7, 40, 94, 1222]
dict1 = {}

for i in range(len(list1)):
    dict1[list1[i]]=list2[i]
print(dict1)

for i in range(len(list1)):
    dict1[list2[i]] = list1[i]