import telebot


bot = telebot.TeleBot("7229103027:AAFDJwsbj6ND7NiM5Emc8yZCyARqR9_5RYw", parse_mode=None)

users = dict()


@bot.message_handler(commands=['start', 'help', 'asd'])
def send_welcome(message):
    if message.from_user.id in users:
        bot.reply_to(message, "Вы зарегистрированы")
    else:
        msg = bot.reply_to(message, "как вас зовут?")
        bot.register_next_step_handler(msg, process_name_step)

def process_name_step(message):
    name = message.text
    msg = bot.reply_to(message, "Сколько вам лет?")
    bot.register_next_step_handler(msg, process_age_step, name)

def process_age_step(message, name):
    user_id = message.from_user.id
    age = message.text



    users[user_id]=name, age
    #reply_to(message, f"Вас зовут {name}, вам {age} лет, ваш telegram id {message.from_user.id}")
    # TODO: Сохранить пользователя





@bot.message_handler(func=lambda m: True)
def answer_all(message):
    print(message.from_user)
    bot.reply_to(message, "echo")


if __name__ == "__main__":
    bot.polling()