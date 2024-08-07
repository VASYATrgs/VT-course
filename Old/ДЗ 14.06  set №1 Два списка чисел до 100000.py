first_input = input("введите числа"   ) # Ввод первого списка
second_input = input("введите числа"  ) # Ввод второго списка
first_list = list(map(int, first_input.split())) # Преобразование первого списка в список целых чисел
second_list = list(map(int, second_input.split())) # Преобразование второго списка в список целых чисел
first_set = set(first_list) # Создание множества из первого списка
second_set = set(second_list) # Создание множества из второго списка
result_set = first_set & second_set # Пересечение множеств
sorted_result = sorted(result_set) # Сортировка результата
for num in sorted_result:
       print(num, end=' ')