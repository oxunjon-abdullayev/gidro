from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.default_citizen_button import cancel_back, user_panel_default_button
from loader import dp, bot
from states.citizen_state import AddUserState





@dp.message_handler(Text(equals="✅ Ro'yxatdan o'tish"))
async def registr_func(message:types.Message):
    await message.answer(text="<b>Xurmatli fuqaro ismingizni kiriting </b>",
                         reply_markup=ReplyKeyboardRemove())
    await AddUserState.name.set()



@dp.message_handler(Text(equals="☎ Bizning aloqa manzil"))
async def phone_address(message:types.Message):
    await message.answer_contact(phone_number="+998 94 355 15 09",
                                 first_name="Medxun",last_name="Sohibov",
                                 disable_notification=True)


@dp.message_handler(Text(equals="📍 Bizning manzil"))
async def location(message:types.Message):
    await message.answer_location(latitude=38.8303042,longitude=65.8080477,
                                  live_period=True)