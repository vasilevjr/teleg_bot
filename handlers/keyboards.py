from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=2
)

register = KeyboardButton("СДЕЛАТЬ ЗАЯВКУ")
contact = KeyboardButton("ОТПРАВЬ КОНТАКТ", request_contact=True)
location = KeyboardButton("ОТПРАВЬ ЛОКАЦИЮ", request_location=True)
quiz = KeyboardButton("/quiz")
techologies = KeyboardButton("/techologies")
info = KeyboardButton("/info")


start_markup.add(register, techologies, location, quiz, contact, info)


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
cancel = KeyboardButton("отмена")
cancel_markup.add(cancel)


gender_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(
    KeyboardButton("МУЖ"),
    KeyboardButton("ЖЕН"),
    cancel
)


sumbit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True

).add(
    KeyboardButton("ДА"),
    KeyboardButton("ИЗМЕНИТЬ"),
    cancel
)