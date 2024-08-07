#1
#Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите все числа,
#которые входят как в первый, так и во второй список в порядке возрастания.

# Решение:
list1 = [12, 13, 14, 1, 15, 17, 1000]
list2 = [1000, 1, 13, 100, 15, 222, 333]
list1_set = set(list1)
list2_set = set(list2)
union_set = list2_set.union(list1_set)
# объединяем списки

list_non_dublicates = list(dict.fromkeys(union_set))
# удаляем дубликаты
list_non_dublicates_sorted = sorted(list_non_dublicates)
# сортируем

print(list_non_dublicates_sorted)

#2
#Напишите программу, которая находит все символы, встречающиеся в обеих переданных ей строках.

m=set(input("введите символы:" ))
n=set(input("введите символы:" ))
a=list(m & n)
a.sort()
print(*a if a!=[] else 'NO', sep='')


# возвращение результата


#3
#Напишите программу, которая для двух последовательностей, состоящих из натуральных чисел, не превосходящих n,
#будет определять, какие числа встречаются в каждой из последовательностей, а какие из чисел от 1 до n — ни в одной из них.


list1 = [ 6, 12,7 ]
list2 = [8, 9, 7]
n = 12
# задаем списки и определяем число n

new_list1 = set(list1)
new_list2 = set(list2)

# преобразуем спсики в множества

union_list_non_dubl = new_list1 | new_list2
# объединям множества и удаляем дубликаты

print("Числа в списках:", union_list_non_dubl)

all_numbers = set(range(1, n + 1))
# Создадим множество всех чисел от 1 до n

missing_numbers = all_numbers - union_list_non_dubl
# Находим числа, которые отсутствуют в объединении множеств

missing_numbers_sorted = sorted(missing_numbers)
# преобразуем результат в отсортированный список


print("Отсутствующие числа:", missing_numbers_sorted)