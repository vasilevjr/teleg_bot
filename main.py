from aiogram import executor
import logging

from config import dp
from handlers import commands, callback, admin, extra, FSM_Admin_clients

commands.register_message_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
FSM_Admin_clients.register_handlers_FSM_Admin_clients(dp)

extra.register_handlers_extra(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)




