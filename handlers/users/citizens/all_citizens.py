from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.default.default_citizen_button import cancel_back
from keyboards.inline.inline_citizen_button import inline_user_button
from loader import dp, db, bot  # , db
from states.citizen_state import ShowAllUserState

@dp.message_handler(Text(equals='cancel'))
async def func_cancel(message:types.Message, state:FSMContext):
    await message.answer_photo(photo='https://www.atf.gov/sites/default/files/media/2015/08/people.jpg',
                         reply_markup=inline_user_button())
    await state.finish()


@dp.callback_query_handler(state=ShowAllUserState.id)
async def all_user(callback:types.CallbackQuery, state: FSMContext):
        user_id = callback.data
        user = db.get_user(id=user_id)
        if callback.data != "back":
            if user:
                await bot.send_location(chat_id=callback.message.chat.id,
                                        latitude=user[5],
                                        longitude=user[6])
                await callback.message.answer(text=
                f"🧾 <b>Fuqaroning ismi  : {user[1]}\n\n"
                f"✅ Fuqaroning yoshi  : {user[2]}\n\n"
                f"📞 Fuqaroning telefon raqami:  {user[3]}\n\n"
                f"🌍 Fuqaroning turar joy manzili  : {user[4]}\n\n</b>",
                                          reply_markup=cancel_back())
                await state.finish()

        elif callback.data == "back":
            await callback.message.answer_photo(photo="https://www.atf.gov/sites/default/files/media/2015/08/people.jpg",
                                          reply_markup=inline_user_button())
            await state.finish()