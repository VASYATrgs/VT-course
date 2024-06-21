#  Возвести каждый элемент списка в квадрат
d = 5
a = [1, 2, 3, 4, 5, 6, 7]
def square(a:list) ->list:
    for g in range(0,len(a)):
        a[g] = a[g]*a[g]
    return (a)
a = square(a)

print(d.real)

print(a)
