from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINS
from . import keyboards
from database.bot_db import sql_command_insert
import re


class ClientsForm(StatesGroup):
    full_name = State()
    phone_number = State()
    city = State()
    address = State()
    sumbit = State()


async def start_clients(message: types.Message):
    if message.chat.type == "private" and message.from_user.id in ADMINS:
        await ClientsForm.full_name.set()
        await message.answer("Добро пожаловать! Для добавления клиента, пожалуйста, введите его ФИО:",
                             reply_markup=keyboards.cancel_markup)
    else:
        await message.answer("Так как вы не являететсь Администратором, Вы не можете заполнять форму ):")


async def process_full_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["full_name"] = message.text
        await ClientsForm.next()
        await message.answer("Введите номер телефона:",
                             reply_markup=keyboards.cancel_markup)

async def validate_phone_number(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)
    if int(len(phone_number) < 10) or int(len(phone_number) > 15):
        return False
    else:
        return True

async def process_number(message: types.Message, state: FSMContext):
    phone_number = message.text
    if await validate_phone_number(phone_number):
        async with state.proxy() as data:
            data["phone_number"] = phone_number
            await ClientsForm.next()
            await message.answer("Введите город:")
    else:
        await message.answer("Некорректный номер телефона. Пожалуйста, введите номер от 10 до 15 цифр.")


async def process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["city"] = message.text
        await ClientsForm.next()
        await message.answer("Введите адрес:")


# async def process_address(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["address"] = message.text
#         await ClientsForm.next()
#         await message.answer("Введите адрес клиента:")

async def process_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["address"] = message.text
        await message.answer(f"ФИО: {data['full_name']}\nНомер: {data['phone_number']}\n"
                             f"Город: {data['city']}\nАдрес: {data['address']}")
        await ClientsForm.next()
        await message.answer("Проверьте все-ли верно?", reply_markup=keyboards.sumbit_markup)


async def sumbit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Спасибо! Данные записаны!")
    elif message.text.lower() == "изменить":
        await ClientsForm.full_name.set()
        await message.answer("Для добавления клиента, напишите пожалуйста ФИО:")
    else:
        await message.answer("Нажмите кнопку")


async def cancle_form(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отмена регистрации")


def register_handlers_FSM_Admin_clients(dp: Dispatcher):
    dp.register_message_handler(cancle_form, state="*", commands=["cancel"])
    dp.register_message_handler(cancle_form, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(start_clients,
                                Text(equals="сделать заявку", ignore_case=True))
    dp.register_message_handler(process_full_name, state=ClientsForm.full_name)
    dp.register_message_handler(process_number, state=ClientsForm.phone_number)
    dp.register_message_handler(process_city, state=ClientsForm.city)
    dp.register_message_handler(process_address, state=ClientsForm.address)
    dp.register_message_handler(sumbit, state=ClientsForm.sumbit)