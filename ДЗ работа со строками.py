string1 = "Иван Сидоров"
first_letter= string1[0]
a = first_letter
slice = string1[5:12]
b= slice
print(a,b)


 #date=input('Enter a date(dd/mm/yyyy)')
 #replace=date.replace('/',' ')
 #convert=replace.split()
 #day=convert[1:2]
 #year=convert[2:4]
 #print("день",day)

date_string = input('Enter a date using the (dd.mm.yyyy) format: ')
date_list = date_string.split('.')
month = date_list[1]
day = date_list[0]
year_ = date_list[2]
print(day, month, ',', year_ )


s="hello world"
slice1=s[0:5]
slice2=s[6:11]
print(slice2, slice1)

print(str(input()).replace(input(),""))


name = str(input("Введите имя: "))
age = int(input("Введите возраст: "))
town = str(input("Введите город: "))
greeting = f"Меня зовут, {name}. Мне {age} лет. Я живу в {town}"
print(greeting)
