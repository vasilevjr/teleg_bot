# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from config import ADMINS
# from . import keyboards
#
# class FSMAdmin(StatesGroup):
#     name = State()
#     age = State()
#     gender = State()
#     region = State()
#     photo = State()
#     submit = State()
#
# async def fsm_start(message: types.Message):
#     if message.chat.type == "private":
#         await FSMAdmin.name.set()
#         await message.answer("Введите имя", reply_markup=keyboards.cancel_markup)
#     else:
#         await message.answer("Вы не являетесь Администратором бота ):")
#
# async def load_name(message: types.Message,state: FSMContext):
#     async with state.proxy() as data:
#         data["name"] = message.text
#     await FSMAdmin.next()
#     await message.answer('Ввидите ')
#
# async def load_age(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["id"] = message.from_user.id
#         data["username"] = f'{message.from_user.username}' if message.from_user.username else None
#         data["full_name"] = message.text
#     await FSMAdmin.next()
#     await message.answer('Пожалуйста введите номер клиента:')
#
# async def load_number(message: types.Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer("Пишите число!")
#     elif not 10 < int(not len(message.text) >= 13:
#         await message.answer("Неправильный ввод!")
#     else:
#         async with state.proxy() as data:
#             data["phone_number"] = message.text
#         await FSMAdmin.next()
#         await message.answer("Пожалуйста введи название своего города:", reply_markup=keyboards.gender_markup )
#
#
# async def city(message: types.Message, state: FSMContext):
#         async with state.proxy() as data:
#             data["city"] = message.text
#         await FSMAdmin.next()
#         await message.answer('Напишите точный адрес доставки:')
#
# async def load_adress(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["adress"] = message.text
#         await message.answer(
#             data["adress"],
#             caption=f"ФИО: {data['name']}\nПолных лет: {data['age']}\nПол: {data['gender']}\n"
#                              f"Место проживания: {data['region']}\n{data['username']}"
#         )
#     await FSMAdmin.next()
#     await message.answer("Все верно?", reply_markup=keyboards.sumbit_markup)
#
# async def sumbit(message: types.Message, state: FSMContext):
#     if message.text.lower() == "да":
#         # TODO: Запись в БД
#         await state.finish()
#         await message.answer("Анкета создана!")
#     elif message.text.lower() == "изменить":
#         await FSMAdmin.name.set()
#         await message.answer("Напишите ФИО")
#     else:
#         await message.answer("Нажмите кнопку")
#
# async def cancle_form(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state:
#         await state.finish()
#         await message.answer("Отмена регистрации")
#
# def register_message_forms(dp: Dispatcher):
#     dp.register_message_handler(cancle_form,
#                                 Text(equals="отмена", ignore_case=True), state="*")
#     dp.register_message_handler(fsm_start,
#                                 Text(equals="зарегистрировать анкету", ignore_case=True))
#     dp.register_message_handler(load_name, state=FSMAdmin.name)
#     dp.register_message_handler(load_age, state=FSMAdmin.age)
#     dp.register_message_handler(load_gender, state=FSMAdmin.gender)
#     dp.register_message_handler(load_region, state=FSMAdmin.region)
#     dp.register_message_handler(load_photo, state=FSMAdmin.photo,
#                                 content_types=["photo"])
#     dp.register_message_handler(sumbit, state=FSMAdmin.submit)

