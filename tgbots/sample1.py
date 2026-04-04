import telebot
import telebot.types

from datetime import datetime

# 8741314074:AAGdFPuHf0DKEJWW8mKmDD804aqFMKbzWB0

bot = telebot.TeleBot("8741314074:AAGdFPuHf0DKEJWW8mKmDD804aqFMKbzWB0")


@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "обработано сообщение старт")


@bot.message_handler(func=lambda message: True)
def message_text_all_handler(message: telebot.types.Message):
    input_text = message.text
    output_text = ""

    if input_text == "привет":
        output_text = "ну привет!"
    elif input_text == "время":
        output_text = str(datetime.now())
    elif input_text == "как тебя зовут":
        output_text = "Я бот 111"
    else:
        output_text = "неизвестная команда"

    bot.send_message(message.chat.id, output_text)


@bot.message_handler(func=lambda message: messahe.text == "пока")



bot.infinity_polling()
# print("бот запущен")
