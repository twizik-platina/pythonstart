

import telebot
from telebot import custom_filters, types
from telebot.states import State, StatesGroup
from telebot.states.sync.context import StateContext
from telebot.states.sync.middleware import StateMiddleware
from telebot.storage import StateMemoryStorage


bot = telebot.TeleBot(
    "8572928625:AAHa0Tz8ZoNdUnvwj3Z3QgMfkGPY49DVfE4",
    state_storage=StateMemoryStorage(),
    use_class_middlewares=True,
)


registrations_dictionary = {}
occupied_slots = {}


class RegistrationStates(StatesGroup):
    main_menu = State()
    input_project_title = State()
    input_student_name = State()
    choose_teacher = State()
    choose_day = State()
    choose_time = State()
    confirm_booking = State()
    choose_edit_field = State()
    edit_project_title = State()
    edit_teacher = State()
    edit_day = State()
    edit_time = State()
    confirm_delete = State()


time_slots = ["15:00", "15:20", "15:40", "16:00", "16:20"]
teachers = ["Иванов", "Петров", "Смирнова"]
days = ["Понедельник", "Вторник", "Среда"]


def show_booking(booking):
    return f"""Имя ученика: {booking['student_name']}
Тема проекта: {booking['project_title']}
Преподаватель: {booking['teacher']}
День: {booking['day']}
Время: {booking['time']}"""


def get_available_slots(teacher, day, exclude_time=None):
    available = []
    for time_slot in time_slots:
        slot_key = (teacher, day, time_slot)
        if slot_key not in occupied_slots or time_slot == exclude_time:
            available.append(time_slot)
    return available


@bot.message_handler(commands=["start"])
def command_start_handler(message: types.Message, state: StateContext):
    output_text = "Добро пожаловать в бот записи на защиту проектов! Выберите действие:"
    
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        ("Записаться на защиту", "button_book"),
        ("Моя запись", "button_my_booking"),
        ("Изменить запись", "button_edit"),
        ("Отменить запись", "button_cancel"),
        ("Показать все записи", "button_show_all")
    ]
    
    for text, callback in buttons:
        keyboard.add(telebot.types.InlineKeyboardButton(text, callback_data=callback))
    
    state.set(RegistrationStates.main_menu)
    bot.send_message(message.chat.id, output_text, reply_markup=keyboard)


@bot.callback_query_handler(state=RegistrationStates.main_menu)
def callback_main_menu_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    
    if call.data == "button_book":
        if user_id in registrations_dictionary:
            bot.send_message(call.message.chat.id, "У вас уже есть запись. Сначала измените или отмените её.")
            return
        state.set(RegistrationStates.input_project_title)
        bot.send_message(call.message.chat.id, "Введите тему проекта (от 3 до 40 символов)")
    
    elif call.data == "button_my_booking":
        if user_id not in registrations_dictionary:
            bot.send_message(call.message.chat.id, "У вас пока нет активной записи.")
        else:
            bot.send_message(call.message.chat.id, f"Ваша запись:\n{show_booking(registrations_dictionary[user_id])}")
    
    elif call.data == "button_edit":
        if user_id not in registrations_dictionary:
            bot.send_message(call.message.chat.id, "У вас пока нет активной записи.")
            return
        
        keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            telebot.types.InlineKeyboardButton("Тему проекта", callback_data="edit_title"),
            telebot.types.InlineKeyboardButton("Преподавателя", callback_data="edit_teacher"),
            telebot.types.InlineKeyboardButton("День и время", callback_data="edit_day_time")
        )
        state.set(RegistrationStates.choose_edit_field)
        bot.send_message(call.message.chat.id, "Что вы хотите изменить?", reply_markup=keyboard)
    
    elif call.data == "button_cancel":
        if user_id not in registrations_dictionary:
            bot.send_message(call.message.chat.id, "У вас пока нет активной записи.")
            return
        
        booking = registrations_dictionary[user_id]
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton("Да", callback_data="confirm_yes"),
            telebot.types.InlineKeyboardButton("Нет", callback_data="confirm_no")
        )
        state.set(RegistrationStates.confirm_delete)
        bot.send_message(call.message.chat.id, f"Вы хотите отменить запись:\n{show_booking(booking)}\n\nТочно отменить запись?", reply_markup=keyboard)
    
    elif call.data == "button_show_all":
        if not registrations_dictionary:
            bot.send_message(call.message.chat.id, "Пока нет ни одной записи.")
        else:
            output = "Список всех записей:\n\n"
            for i, (uid, booking) in enumerate(registrations_dictionary.items(), 1):
                output += f"{i}.\n{show_booking(booking)}\n\n"
            bot.send_message(call.message.chat.id, output)


@bot.message_handler(state=RegistrationStates.input_project_title)
def message_project_title_handler(message: types.Message, state: StateContext):
    title = message.text.strip()
    if len(title) < 3 or len(title) > 40:
        bot.send_message(message.chat.id, "Ошибка. Длина темы проекта должна быть от 3 до 40 символов\nВведите тему ещё раз")
        return
    state.add_data(project_title=title)
    state.set(RegistrationStates.input_student_name)
    bot.send_message(message.chat.id, "Введите имя ученика (от 2 до 30 символов)")


@bot.message_handler(state=RegistrationStates.input_student_name)
def message_student_name_handler(message: types.Message, state: StateContext):
    name = message.text.strip()
    if len(name) < 2 or len(name) > 30:
        bot.send_message(message.chat.id, "Ошибка. Длина имени должна быть от 2 до 30 символов\nВведите имя ещё раз")
        return
    state.add_data(student_name=name)
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    for teacher in teachers:
        keyboard.add(telebot.types.InlineKeyboardButton(teacher, callback_data=teacher))
    
    state.set(RegistrationStates.choose_teacher)
    bot.send_message(message.chat.id, "Выберите преподавателя:", reply_markup=keyboard)


@bot.callback_query_handler(state=RegistrationStates.choose_teacher)
def callback_teacher_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    state.add_data(teacher=call.data)
    
    keyboard = telebot.types.InlineKeyboardMarkup()
    for day in days:
        keyboard.add(telebot.types.InlineKeyboardButton(day, callback_data=day))
    
    state.set(RegistrationStates.choose_day)
    bot.send_message(call.message.chat.id, "Выберите день:", reply_markup=keyboard)


@bot.callback_query_handler(state=RegistrationStates.choose_day)
def callback_day_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    state.add_data(day=call.data)
    
    with state.data() as data:
        available = get_available_slots(data["teacher"], call.data)
    
    if not available:
        bot.send_message(call.message.chat.id, "На этот день нет свободных слотов. Выберите другой день.")
        return
    
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    for slot in available:
        keyboard.add(telebot.types.InlineKeyboardButton(slot, callback_data=slot))
    
    state.set(RegistrationStates.choose_time)
    bot.send_message(call.message.chat.id, "Выберите свободное время:", reply_markup=keyboard)


@bot.callback_query_handler(state=RegistrationStates.choose_time)
def callback_time_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    
    with state.data() as data:
        slot_key = (data["teacher"], data["day"], call.data)
    
    if slot_key in occupied_slots:
        bot.send_message(call.message.chat.id, "Этот слот уже занят. Выберите другое время.")
        return
    
    state.add_data(time=call.data)
    
    with state.data() as data:
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton("Да", callback_data="confirm_yes"),
            telebot.types.InlineKeyboardButton("Нет", callback_data="confirm_no")
        )
        
        state.set(RegistrationStates.confirm_booking)
        bot.send_message(call.message.chat.id, 
            f"Проверьте правильность введённых данных:\n{show_booking(data)}\n\nПодтвердить запись?",
            reply_markup=keyboard)


@bot.callback_query_handler(state=RegistrationStates.confirm_booking)
def callback_confirm_booking_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    
    if call.data == "confirm_yes":
        with state.data() as data:
            slot_key = (data["teacher"], data["day"], data["time"])
            if slot_key in occupied_slots:
                bot.send_message(call.message.chat.id, "Ошибка! Слот уже занят. Запись не сохранена.")
                state.delete()
                return
            
            registrations_dictionary[user_id] = dict(data)
            occupied_slots[slot_key] = user_id
        
        bot.send_message(call.message.chat.id, "Запись успешно сохранена!\nНажмите /start для перехода в главное меню")
    else:
        bot.send_message(call.message.chat.id, "Запись отменена\nНажмите /start для перехода в главное меню")
    
    state.delete()



@bot.callback_query_handler(state=RegistrationStates.choose_edit_field)
def callback_choose_edit_field_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    
    if call.data == "edit_title":
        state.set(RegistrationStates.edit_project_title)
        bot.send_message(call.message.chat.id, "Введите новую тему проекта (от 3 до 40 символов)")
    
    elif call.data == "edit_teacher":
        keyboard = telebot.types.InlineKeyboardMarkup()
        for teacher in teachers:
            keyboard.add(telebot.types.InlineKeyboardButton(teacher, callback_data=teacher))
        state.set(RegistrationStates.edit_teacher)
        bot.send_message(call.message.chat.id, "Выберите нового преподавателя:", reply_markup=keyboard)
    
    elif call.data == "edit_day_time":
        keyboard = telebot.types.InlineKeyboardMarkup()
        for day in days:
            keyboard.add(telebot.types.InlineKeyboardButton(day, callback_data=day))
        state.set(RegistrationStates.edit_day)
        bot.send_message(call.message.chat.id, "Выберите день:", reply_markup=keyboard)


@bot.message_handler(state=RegistrationStates.edit_project_title)
def message_edit_title_handler(message: types.Message, state: StateContext):
    title = message.text.strip()
    if len(title) < 3 or len(title) > 40:
        bot.send_message(message.chat.id, "Ошибка. Длина темы должна быть от 3 до 40 символов\nВведите тему ещё раз")
        return
    
    user_id = message.from_user.id
    registrations_dictionary[user_id]["project_title"] = title
    bot.send_message(message.chat.id, f"Запись успешно изменена!\n{show_booking(registrations_dictionary[user_id])}\n\nНажмите /start")
    state.delete()


@bot.callback_query_handler(state=RegistrationStates.edit_teacher)
def callback_edit_teacher_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    old_booking = registrations_dictionary[user_id]
    

    old_slot = (old_booking["teacher"], old_booking["day"], old_booking["time"])
    if old_slot in occupied_slots:
        del occupied_slots[old_slot]
    
    registrations_dictionary[user_id]["teacher"] = call.data
    new_slot = (call.data, old_booking["day"], old_booking["time"])
    occupied_slots[new_slot] = user_id
    
    bot.send_message(call.message.chat.id, f"Запись успешно изменена!\n{show_booking(registrations_dictionary[user_id])}\n\nНажмите /start")
    state.delete()


@bot.callback_query_handler(state=RegistrationStates.edit_day)
def callback_edit_day_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    state.add_data(new_day=call.data)
    user_id = call.from_user.id
    teacher = registrations_dictionary[user_id]["teacher"]
    
    available = get_available_slots(teacher, call.data)
    
    if not available:
        bot.send_message(call.message.chat.id, "На этот день нет свободных слотов. Выберите другой день.")
        return
    
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    for slot in available:
        keyboard.add(telebot.types.InlineKeyboardButton(slot, callback_data=slot))
    
    state.set(RegistrationStates.edit_time)
    bot.send_message(call.message.chat.id, "Выберите новое время:", reply_markup=keyboard)


@bot.callback_query_handler(state=RegistrationStates.edit_time)
def callback_edit_time_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    old_booking = registrations_dictionary[user_id]
    
    with state.data() as data:
        new_day = data["new_day"]
    
    slot_key = (old_booking["teacher"], new_day, call.data)
    
    if slot_key in occupied_slots:
        bot.send_message(call.message.chat.id, "Этот слот уже занят. Выберите другое время.")
        return
    

    old_slot = (old_booking["teacher"], old_booking["day"], old_booking["time"])
    if old_slot in occupied_slots:
        del occupied_slots[old_slot]
    
    registrations_dictionary[user_id]["day"] = new_day
    registrations_dictionary[user_id]["time"] = call.data
    occupied_slots[slot_key] = user_id
    
    bot.send_message(call.message.chat.id, f"Запись успешно изменена!\n{show_booking(registrations_dictionary[user_id])}\n\nНажмите /start")
    state.delete()


@bot.callback_query_handler(state=RegistrationStates.confirm_delete)
def callback_confirm_delete_handler(call: types.CallbackQuery, state: StateContext):
    bot.answer_callback_query(call.id)
    user_id = call.from_user.id
    
    if call.data == "confirm_yes":
        booking = registrations_dictionary[user_id]
        slot_key = (booking["teacher"], booking["day"], booking["time"])
        if slot_key in occupied_slots:
            del occupied_slots[slot_key]
        del registrations_dictionary[user_id]
        bot.send_message(call.message.chat.id, "Запись успешно отменена\nНажмите /start")
    else:
        bot.send_message(call.message.chat.id, "Отмена записи отменена\nНажмите /start")
    
    state.delete()


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))

bot.infinity_polling()