from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.inline_citizen_button import inline_user_button
from loader import dp #, db
from states.citizen_state import ShowAllUserState


@dp.callback_query_handler(state=ShowAllUserState.id)
async def all_user(callback:types.CallbackQuery, state: FSMContext):
        user_id = callback.data
        # user = db.get_user(id=user_id)
        # if callback.data != "back":
        #     if user:
        #         await callback.message.answer(text=
        #         f"<b>📍 <i>Fuqaroning GES qurmoqchi bo'lgan manzili</i> : {user[5]}\n\n"
        #         f"🧾 Fuqaroning ismi  : {user[1]}\n\n"
        #         f"✅ Fuqaroning yoshi  : {user[2]}\n\n"
        #         f"📞 Fuqaroning telefon raqami:  {user[3]}\n\n"
        #         f"🌍 Fuqaroning turar joy manzili  : {user[4]}\n\n</b>",
        #                                   reply_markup=inline_user_button())
        #         await state.finish()
        #
        # elif callback.data == "back":
        #     await callback.message.answer_photo(photo="https://www.atf.gov/sites/default/files/media/2015/08/people.jpg",
        #                                   reply_markup=inline_user_button())
        #     await state.finish()