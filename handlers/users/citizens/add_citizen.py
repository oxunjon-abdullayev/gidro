from aiogram import types
from aiogram.dispatcher import FSMContext
import re

from data.config import ADMINS
from keyboards.default.default_citizen_button import user_panel_default_button
from loader import dp, bot, db
from states.citizen_state import AddUserState


@dp.message_handler(state=AddUserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer(text="<b><em>✅ Yoshingizni kiriting</em></b>")
    await AddUserState.next()


@dp.message_handler(state=AddUserState.age)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['age'] = int(message.text)
            await message.answer(text="<b><em>📞 Telefon raqamingizni kiriting</em></b>")
            await AddUserState.next()

        except ValueError:
            await message.answer("<b><em>✅ Yosh butun son bo'lsin</em></b>")


@dp.message_handler(state=AddUserState.phone_number)
async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        PHONE_REGEX = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
        phone_number = re.match(PHONE_REGEX, message.text)
        if phone_number:
            data['phone_number'] = message.text

            await AddUserState.next()
            await message.answer("<b><em>🏠 Yashash turar-joy manzilingingizni kiriting</em></b>")
        else:
            await message.answer("<b>Telefon raqam xato kiritildi</b>")


@dp.message_handler(state=AddUserState.address)
async def add_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text

    await AddUserState.next()
    await message.answer("💧 GES   <em>qurmoqchi bo'lgan manzilingizning locatsiyasini kiriting</em>")


@dp.message_handler(state=AddUserState.location)
async def check_location(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['location'] = message.text
    await bot.send_message(chat_id=ADMINS[0],
                           text=
                                f"Fuqaroning <b>GES</b> qurmoqchi bo'lan manzil locatsiyasi : {data['location']}\n\n"
                                  f"🧾 Fuqaroning ismi  :{data['name']}\n\n"
                                           f"✅ Fuqaroning yoshi : {data['age']}\n\n"
                                           f"📞 Fuqaroning telefon raqami :{data['phone_number']}\n\n"
                                           f"🌐 Fuqaroning turar joy manzili  :{data['address']}\n\n")

    db.add_user(name=data['name'],
                          age=data['age'],
                          phone_number=data['phone_number'],
                          address=data['address'],
                          location=data['location'])

    await message.answer(text="ma'lumotlaringiz saqlandi",
                         reply_markup=user_panel_default_button())
    await state.finish()





