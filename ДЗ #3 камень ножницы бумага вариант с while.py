import random

comp_turn = ['k', 'b', 'n']
gameloop: bool = True
while gameloop:
    turn = input('k-kamen, n - nognici, b - bumaga, exit - выход')
    if turn == 'k': print("kamen")
    elif turn == 'b': print("bumaga")
    elif turn == 'n': print("nognici")
    elif turn == 'exit':
        print('выход')
        gameloop = False
    c_turn = random.choice(comp_turn)
    if turn == 'k' and c_turn == 'n':
          print("ты выиграл")
    if turn == 'n' and c_turn == 'b':
          print("ты выиграл")
    if turn == 'b' and c_turn == 'k':
          print("ты выиграл")
    if turn == 'b' and c_turn == 'n':
          print("комп выиграл")
    if turn == 'k' and c_turn == 'b':
          print("комп выиграл")
    if turn == 'n' and c_turn == 'k':
          print("комп выиграл")