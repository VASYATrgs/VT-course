import random, time

comp_turn = ['k', 'b', 'n']
count = [0, 0]
def knb_choise(t):
    if t == 'k':
        print("kamen")
    elif t == 'b':
        print("bumaga")
    elif t == 'n':
        print("nognici")
def main():
    gameloop: bool = True
    while gameloop:
        turn = input('k-kamen, n - nognici, b - bumaga, exit - выход')
        print()
        time.sleep(1)
        if turn == 'exit':
            print('выход')
        else:
            knb_choise(turn)
            gameloop = False
            c_turn = random.choice(comp_turn)
            knb_choise(c_turn)
            if (turn == 'k' and c_turn == 'n') or (turn == 'n' and c_turn == 'b') or (turn == 'b' and c_turn == 'k'):
                  print("ты выиграл")
                  count[0] += 1
            if (turn == 'b' and c_turn == 'n') or (turn == 'k' and c_turn == 'b') or (turn == 'n' and c_turn == 'k'):
                  print("комп выиграл")
                  count[1] += 1
        print('счет - ', count[0],':', count[1])
if __name__== '__main__':
    main()