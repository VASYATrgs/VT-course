#2 Напишите программу, которая запрашивает у пользователя числа до тех пор,
while True:
  output = ""
  num = int(input("введите число: "))

  if num == 0:
    exit()

  for i in range(1, num+1):
    output += "{}".format(i)
    if i != num:
      output += "+"
  output += " = {}".format(sum(range(num+1)))
  print (output)