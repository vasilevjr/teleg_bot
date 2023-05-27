from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from requests import get
from .keyboards import start_markup


async def start_hendler(message: types.Message):
    await message.answer(F"Приветствуем Вас - {message.from_user.full_name}!",
                         reply_markup=start_markup)


async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "В каком году Ново-Лядовская начала обеспечивать кристально " \
               "чистой водой жителей Пермского края?"
    answers = [
       "1995",
       "2000",
       "2001",
       "2023",
       "2004",
       "2030",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type="quiz",
        correct_option_id=0,
        open_period=11,
        reply_markup=markup
    )

# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Сколько раз была награждена золотыми и " \
               "серебрянными медалями за вкус и качество Ново-Лядовская вода?"
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
        open_period=11
    )

async def message_hendler_photo(message: types.Message):
    await bot.send_message(message.chat.id, "В нашей компании принципиально не "
                                            "применяется технология обратного "
                                            "осмоса, которая делает воду «неживой».")
    await  bot.send_photo(message.chat.id, get("https://voda59.ru/assets/template/"
                                               "water/resources/img/content/about/make/make_bg.jpg").content)

async def info_hendler(message: types.Message):
    await message.answer(F'Сам разбирайся!')


def register_message_commands(dp: Dispatcher):
    dp.register_message_handler(start_hendler, commands=["start", "help"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(message_hendler_photo, commands=["techologies"])
    dp.register_message_handler(info_hendler, commands=["info"])