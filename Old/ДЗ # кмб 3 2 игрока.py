
while True: # обратите внимание на эту строку кода
    count = [0, 0]
    user_action = input("Игрок 1 Сделайте выбор — камень, ножницы или бумага: ")
    possible_actions = ["камень", "бумага", "ножницы"]
    user2_action = input("Игрок 2 Сделайте выбор — камень, ножницы или бумага: ")
    print(f'\nВы выбрали {user_action}, пользователь2 выбрал {user2_action}.\n')
    if user_action == user2_action:
        print(f"Оба пользователя выбрали {user_action}. Ничья!!")
    elif user_action == "камень":
        if user2_action == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
            count[0] += 1
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
            count[1] += 1
    elif user_action == "бумага":
        if user2_action == "камень":
            print("Бумага оборачивает камень! Вы победили!")
            count[0] += 1
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
            count[1] += 1
    elif user_action == "ножницы":
        if user2_action == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
            count[0] += 1
        else:
            print("Камень бьет ножницы! Вы проиграли.")
            count[1] += 1
            # а также обратите внимание на код ниже
    print('счет - ', count[0],':', count[1])
    play_again = ""
    play_again = input("Сыграем еще? (д/н): ")
    if play_again.lower() != "д":
        break