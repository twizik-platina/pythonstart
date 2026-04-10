
import telebot
from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage


bot = telebot.TeleBot(
    "8342317228:AAFEszGG99wORBRp1Aio-38uFXfxUKwQu_o",
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)


registrations_dictionary = {}


class RegistrationStates(StatesGroup):
    main_menu_buttons_press = State()
    input_student_name = State()
    input_student_age = State()
    input_course_direction = State()
    save_student_data = State()


@bot.message_handler(commands=["start"])
def command_start_handler(message: types.Message, state: StateContext):

    output_text = "Добро пожаловать в бот записи на пробное занятие! Выберите действие:"

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_add_student = telebot.types.InlineKeyboardButton(
        "Записаться на занятие", callback_data="button_add_student"
    )
    button_show_all_students = telebot.types.InlineKeyboardButton(
        "Показать все записи", callback_data="button_show_all_students"
    )

    inline_reply_keyboard.add(button_add_student)
    inline_reply_keyboard.add(button_show_all_students)

    state.set(RegistrationStates.main_menu_buttons_press)

    bot.send_message(message.chat.id, output_text, reply_markup=inline_reply_keyboard)


@bot.callback_query_handler(state=RegistrationStates.main_menu_buttons_press)
def callback_buttons_main_menu_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    if call.data == "button_add_student":
        output_text = "Введите имя ученика (от 2 до 20 символов)"

        state.set(RegistrationStates.input_student_name)

        bot.send_message(call.message.chat.id, output_text)
    
    elif call.data == "button_show_all_students":
        if not registrations_dictionary:
            output_text = "Пока нет ни одной записи."
        else:
            output_text = "Список записей:\n"
            counter = 1
            for user_id, student_data in registrations_dictionary.items():
                output_text += f"{counter}. \nИмя: {student_data['student_name']}\nВозраст: {student_data['student_age']}\nНаправление: {student_data['course_direction']}\n\n"
                counter += 1
        
        bot.send_message(call.message.chat.id, output_text)


@bot.message_handler(state=RegistrationStates.input_student_name)
def message_text_student_name_handler(message: types.Message, state: StateContext):
    student_name = message.text.strip()

    if len(student_name) < 2 or len(student_name) > 20:
        output_text = "Ошибка. Длина имени должна быть от 2 до 20 символов\nВведите имя ещё раз"
        bot.send_message(message.chat.id, output_text)
        return

    state.add_data(student_name=student_name)

    output_text = "Введите возраст ученика (от 7 до 17 лет): "

    state.set(RegistrationStates.input_student_age)

    bot.send_message(
        message.chat.id,
        output_text,
    )


@bot.message_handler(state=RegistrationStates.input_student_age)
def message_text_student_age_handler(message: types.Message, state: StateContext):
    student_age_as_text = message.text.strip()

    if student_age_as_text.isdigit() == False:
        output_text = "Ошибка. Вы ввели НЕ число. Попробуйте ещё раз:"
        bot.send_message(message.chat.id, output_text)
        return

    student_age = int(student_age_as_text)

    if student_age < 7 or student_age > 17:
        output_text = "Ошибка. Возраст ученика должен быть от 7 до 17 лет"
        bot.send_message(message.chat.id, output_text)
        return

    state.add_data(student_age=student_age)

    output_text = "Выберите направление обучения"

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_python = telebot.types.InlineKeyboardButton(
        "Python", callback_data="Python"
    )
    button_web = telebot.types.InlineKeyboardButton(
        "Web-разработка", callback_data="Web-разработка"
    )
    button_games = telebot.types.InlineKeyboardButton(
        "Разработка игр", callback_data="Разработка игр"
    )

    inline_reply_keyboard.add(button_python)
    inline_reply_keyboard.add(button_web)
    inline_reply_keyboard.add(button_games)

    state.set(RegistrationStates.input_course_direction)

    bot.send_message(message.chat.id, output_text, reply_markup=inline_reply_keyboard)


@bot.callback_query_handler(state=RegistrationStates.input_course_direction)
def callback_buttons_course_direction_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    state.add_data(course_direction=call.data)

    with state.data() as data:
        student_name = data["student_name"]
        student_age = data["student_age"]
        course_direction = data["course_direction"]

    output_text = f"""
Проверьте правильность введённых данных
Имя ученика: {student_name}
Возраст: {student_age}
Направление: {course_direction}

Сохранить запись?
"""

    inline_reply_keyboard = telebot.types.InlineKeyboardMarkup()

    button_yes = telebot.types.InlineKeyboardButton("Да", callback_data="button_yes")
    button_no = telebot.types.InlineKeyboardButton("Нет", callback_data="button_no")

    inline_reply_keyboard.add(button_yes)
    inline_reply_keyboard.add(button_no)

    state.set(RegistrationStates.save_student_data)

    bot.send_message(
        call.message.chat.id, output_text, reply_markup=inline_reply_keyboard
    )


@bot.callback_query_handler(state=RegistrationStates.save_student_data)
def callback_buttons_save_student_data_handler(
    call: types.CallbackQuery, state: StateContext
):
    bot.answer_callback_query(call.id)

    if call.data == "button_yes":
        user_id = call.from_user.id

        with state.data() as data:
            registrations_dictionary[user_id] = {
                "student_name": data["student_name"],
                "student_age": data["student_age"],
                "course_direction": data["course_direction"],
            }

        output_text = "Запись успешно сохранена\nНажмите /start для перехода в главное меню"

    elif call.data == "button_no":

        output_text = "Запись отменена\nНажмите /start для перехода в главное меню"

    state.delete()

    bot.send_message(call.message.chat.id, output_text)


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

bot.infinity_polling()