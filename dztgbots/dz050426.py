import telebot
import telebot.types

from datetime import datetime

bot = telebot.TeleBot("8393470030:AAGyjf0L_spQemba0OdCU410HGlsnB32Phc")


# расписание для каждого дня
schedule = {
    "понедельник": "Понедельник:\n1. Математика\n2. Русский язык\n3. Информатика",
    "вторник": "Вторник:\n1. Физика\n2. Химия\n3. Биология",
    "среда": "Среда:\n1. История\n2. Обществознание\n3. География",
    "четверг": "Четверг:\n1. Литература\n2. Английский язык\n3. Физкультура",
    "пятница": "Пятница:\n1. Музыка\n2. ИЗО\n3. Технология"
}


@bot.message_handler(commands=["start"])
def command_start_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Привет! Я бот с расписанием. Напиши /schedule")


@bot.message_handler(commands=["schedule"])
def command_schedule_handler(message: telebot.types.Message):

    reply_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    

    button_monday = telebot.types.KeyboardButton("Понедельник")
    button_tuesday = telebot.types.KeyboardButton("Вторник")
    button_wednesday = telebot.types.KeyboardButton("Среда")
    button_thursday = telebot.types.KeyboardButton("Четверг")
    button_friday = telebot.types.KeyboardButton("Пятница")
    

    reply_keyboard.add(button_monday)
    reply_keyboard.add(button_tuesday)
    reply_keyboard.add(button_wednesday)
    reply_keyboard.add(button_thursday)
    reply_keyboard.add(button_friday)
    
    bot.send_message(message.chat.id, "Выбери день недели:", reply_markup=reply_keyboard)


@bot.message_handler(func=lambda message: message.text == "Понедельник")
def handle_monday(message: telebot.types.Message):
    bot.send_message(message.chat.id, schedule["понедельник"])


@bot.message_handler(func=lambda message: message.text == "Вторник")
def handle_tuesday(message: telebot.types.Message):
    bot.send_message(message.chat.id, schedule["вторник"])


@bot.message_handler(func=lambda message: message.text == "Среда")
def handle_wednesday(message: telebot.types.Message):
    bot.send_message(message.chat.id, schedule["среда"])


@bot.message_handler(func=lambda message: message.text == "Четверг")
def handle_thursday(message: telebot.types.Message):
    bot.send_message(message.chat.id, schedule["четверг"])


@bot.message_handler(func=lambda message: message.text == "Пятница")
def handle_friday(message: telebot.types.Message):
    bot.send_message(message.chat.id, schedule["пятница"])


@bot.message_handler(func=lambda message: True)
def message_text_all_handler(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Я не знаю такого дня. Выбери день через кнопки.")


bot.infinity_polling()