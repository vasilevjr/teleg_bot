from aiogram import types, Dispatcher, Bot, executor
from config import bot, dp, ADMINS
from asyncio import sleep


async def dice_game2(message: types.Message):
    if message.chat.type == "private" and message.from_user.id in ADMINS:
        await bot.send_message(message.from_user.id, f"Саламчик, "
                                                 f"{message.from_user.full_name}\n"
                                                 f"крч, ща в кости сыграем")
        await sleep(2)
    else:
        await message.answer("Ты не админ, тебе нельзя ):")



    await bot.send_message(message.from_user.id, "Бот кидает!")
    bot_data = await bot.send_dice(message.from_user.id)
    bot_data = bot_data["dice"]["value"]
    await sleep(5)


    await bot.send_message(message.from_user.id, "Кидаешь ты!")
    user_data = await bot.send_dice(message.from_user.id)
    user_data = user_data["dice"]["value"]
    await sleep(5)

    if bot_data > user_data:
        await bot.send_message(message.from_user.id, f"{message.from_user.full_name}\nТы проеал!")
    elif bot_data < user_data:
        await bot.send_message(message.from_user.id, f"{message.from_user.full_name}\nНе ссы,ты выеал!")
    else:
        await bot.send_message(message.from_user.id, "Нечьи не бывает, всё уйня давай по новой!")








def register_handlers_dice_game(dp: Dispatcher):
    dp.register_message_handler(dice_game2, commands=["dice"])
    #регистрируем функции
