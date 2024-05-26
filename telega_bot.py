import telebot
from telebot import types

bot = telebot.TeleBot("7327339355:AAEbsoAHWysCyMQmPhQI1xHQzq6-iLczRHo")
name = ""
surename = ""
age = 0


@bot.message_handler(content_types=["text"])

def start(message):
    if message.text == "Привет" or message.text=="привет" or message.text=="hi":
        bot.send_message(message.from_user.id, "Привет! А как тебя зовут? ")
        bot.register_next_step_handler(message, dialog1)
    else:
        bot.send_message(message.from_user.id, "Не понял. Повтори пожалуйста еще раз!")


def dialog1(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у тебя фамилия?")
    bot.register_next_step_handler(message, dialog2)


def dialog2(message):
    global surename
    surename = message.text
    bot.send_message(message.from_user.id, "Сколько тебе лет? ")
    bot.register_next_step_handler(message, dialog3)


def dialog3(message):
    global age
    age = message.text
    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
    keyboard.add(yes)
    no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyboard.add(no)

    question = "фамилия и имя : "+name + " " + surename + "\n Возраст: "+str(age) + "\nВерно?"
    
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(
            call.message.chat.id,
            "Отлично! Рад знакомству! Я очень спешу, потом поговорим. Пока!",
        )
    elif call.data == "no":
        bot.send_message(
            call.message.chat.id, "Ладно Тогда познакомимся в другой раз Пока!"
        )
        bot.send_message(
            call.message.chat.id, "Напишите снова 'Привет' для начала диалога "
        )


bot.polling(none_stop=True, interval=0)

