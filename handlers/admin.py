from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, ADMINS
from database.bot_db import sql_command_all, sql_command_delete

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


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await message.answer(f"{user[1]}\n{user[2]}\n"
                             f"{user[3]}\n{user[-1]}",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(f"Delete {user[1]}",
                                                      callback_data=f"delete {user[0]}")
                             ))


async def complete_delete(callback: types.CallbackQuery):
    await sql_command_delete(callback.data.split()[1])
    await callback.answer("Удалено!", show_alert=True)
    await callback.message.delete()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=["ban"], commands_prefix="!/")
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix="!/")
    dp.register_message_handler(delete_data, commands=["del"])
    dp.register_callback_query_handler(
        complete_delete,
        lambda callback: callback.data and callback.data.startswith("delete ")
        )