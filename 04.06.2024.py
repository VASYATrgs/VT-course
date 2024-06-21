# Написать аннотацию к функции substituion:
# number_1, number_2, number_3 - целые числа
# is_print - Логическая переменная True/False
# goodbye_word - строка
# возвращает число с плавающей точкой


def substituion(number_1: int, number_2: int, number_3: int, is_print: bool=False, goodbye_word: str="default") -> float:
    if is_print:
        print(goodbye_word)

    return number_1 / number_2 / number_3


result = substituion(
    number_1=1000, number_2=10, number_3=31, is_print=True, goodbye_word="yt"
)

print(result)