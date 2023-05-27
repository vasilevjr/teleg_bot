import random

from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    bad_words = ["fuck", "html", "js"]
    username = f"@{message.from_user.username}"\
        if message.from_user.username else message.from_user.full_name
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            # await bot.delete_message(message.chat.id, message.message_id)
            await message.delete()
            await message.answer(
                f"Не матерись! {username}, сам ты {word}!"
            )


    if message.text.startswith("game"):
        emojis = ['🎮', '🎰', '🎯', '🏀', '🎲','⚽️']
        random_emojis = random.choice(emojis)
        await message.reply(random_emojis)


    if message.text.startswith("."):
        await message.pin()


    if message.text == "гейм":
        a = await bot.send_dice(message.chat.id, emoji="🎲")
        print(a.dice.values)


    try:
        number = int(message.text)
        squared_number = number ** 2
        response = str(squared_number)

    except ValueError:
        response = message.text

    await bot.send_message(chat_id=message.chat.id, text=response)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)


