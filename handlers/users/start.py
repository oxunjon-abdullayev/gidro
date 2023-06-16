from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.default_citizen_button import user_rkm, user_panel_default_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    if message.from_user.id == 1295742159:
        await message.answer(text=f"Admin xush kelibsiz !",
                             reply_markup=user_rkm())
    else:
        await message.answer(f"Salom, {message.from_user.full_name}!",
                             reply_markup=user_panel_default_button())



#
# @dp.message_handler(CommandStart(),IsAdmin())
# async def bot_start(message: types.Message):
#     await message.answer(text=f"Admin xush kelibsiz !",
#                              reply_markup=user_rkm())

# @dp.message_handler(CommandStart())
# async def bot_user_start(message:types.Message):
#         await message.answer(f"Salom, {message.from_user.full_name}!",
#                              reply_markup=user_panel_default_button())