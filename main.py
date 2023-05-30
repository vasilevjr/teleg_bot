from aiogram import executor
import logging

from config import dp, bot, ADMINS
from handlers import commands, callback, admin, extra, FSM_Admin_clients, dice_games
from database.bot_db import sql_create

async def on_startup(db):
    await bot.send_message(ADMINS[0], "Я включен!")
    sql_create()

async def on_shutdown(dp):
    await bot.send_message(ADMINS[0], "Я выключен!")
    sql_create()


commands.register_message_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
FSM_Admin_clients.register_handlers_FSM_Admin_clients(dp)
dice_games.register_handlers_dice_game(dp)

extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup, on_shutdown=on_shutdown)




