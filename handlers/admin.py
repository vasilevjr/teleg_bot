from aiogram import types, Dispatcher
from config import bot, ADMINS

async def ban(message: types.Message):
    if message.chat.id != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Комагда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(
                f'{message.from_user.first_name} братан кикнул'
                f'{message.reply_to_message.from_user.full_name}'
            )
    else:
        await message.answer("Пиши в группе!")

async def pin_message(message: types.Message):
    if message.reply_to_message:
        chat_id = message.chat.id
        message_id = message.reply_to_message.message_id

        try:
            await bot.pin_chat_message(chat_id=chat_id, message_id=message_id)
            await message.answer("Сообщение закреплено!")
        except Exception as e:
            await message.answer (f"Не удалось закрепить сообщение: {str(e)}")
        else:
            await message.answer("Эта команда должна быть ответом на другое сообщение!")

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix="!/")
