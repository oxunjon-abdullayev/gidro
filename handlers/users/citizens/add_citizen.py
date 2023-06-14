from aiogram import types
from aiogram.dispatcher import FSMContext
import re

from aiogram.types import Location

from keyboards.default.default_citizen_button import user_panel_default_button, user_location
from loader import dp, bot, db
from states.citizen_state import AddUserState


@dp.message_handler(state=AddUserState.name)
async def add_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_text =message.text
        NAME = re.match(r'^[a-zA-Z\s.,?!\'"]*$', user_text)
        if NAME:
            data['name'] = message.text
            await message.answer(text="<b><em>✅ Yoshingizni kiriting</em></b>")
            await AddUserState.next()

        else:
            await message.answer(text="<b>Ismni kiritishda xatolik bor</b>")


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
    await message.answer("💧 <b>GES</b> <em>qurmoqchi bo'lgan manzilingizning locatsiyasini kiriting</em>",
                         reply_markup=user_location())



@dp.message_handler(state=AddUserState.location, content_types=['location'])
async def check_location(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        location: Location = message.location
        data['latitude'] = location.latitude
        data['longitude'] = location.longitude
    await bot.send_location(chat_id=message.chat.id,
                            latitude=data['latitude'],
                            longitude=data['longitude'])
    await bot.send_message(chat_id=message.chat.id,
                           text=  f"<b>🧾 Fuqaroning ismi  :{data['name']}\n\n"
                                           f"✅ Fuqaroning yoshi : {data['age']}\n\n"
                                           f"📞 Fuqaroning telefon raqami :{data['phone_number']}\n\n"
                                           f"🌐 Fuqaroning turar joy manzili  :{data['address']}\n\n</b>")

    db.add_user(name=data['name'],
                          age=data['age'],
                          phone_number=data['phone_number'],
                          address=data['address'],
                          latitude=data['latitude'],
                          longitude=data['longitude'])

    await message.answer(text="ma'lumotlaringiz saqlandi",
                         reply_markup=user_panel_default_button())
    await state.finish()





