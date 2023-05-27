from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot

async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_2)

    question = "Сколько раз была награждена золотыми и серебрянными медалями за вкус и качество Ново-Лядовская вода ?"
    answers = [
        "9 медалей",
        "21 медаль",
        "28 медалей",
        "14 медалей",
        "17 медалей",
        "108 медалей",
        ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=11,
        reply_markup=markup
    )

async def quiz_3(message: types.Message):
    question = "На какой глубине расположена скважена ?"
    answers = [
        "100 метров",
        "55 метров",
        "74 метра",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=2,
        open_period=11
    )

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")


