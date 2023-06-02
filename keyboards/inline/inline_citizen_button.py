from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db


def inline_user_button():
    ikm = InlineKeyboardMarkup(row_width=1)
    button2 = InlineKeyboardButton(text="✅ Ro'yxatdan o'tgan foydalanuvchilar", callback_data="all_user")
    button5 = InlineKeyboardButton(text="✅ Ro'yxatdan biror bir fuqaroni o'chirish", callback_data="delete_user")
    ikm.add(button2, button5)
    return ikm


def confirm():
    ikm = InlineKeyboardMarkup(row_width=2)
    btn = InlineKeyboardButton("👍 Ha ", callback_data="ha")
    btn2 = InlineKeyboardButton("👎 Yo'q ", callback_data="yo'q")
    ikm.add(btn, btn2)
    return ikm


def show_users():
    ikm = InlineKeyboardMarkup()
    for i in db.all_user():
        button = InlineKeyboardButton(text=f"{i[1]}",callback_data=f"{i[0]}")
        ikm.add(button)
    button1= InlineKeyboardButton(text="🛒 Back to home",
                                  callback_data="back")
    ikm.add(button1)
    return ikm



def delete_user_button():
    ikm = InlineKeyboardMarkup()
    for i in db.all_user():
        button = InlineKeyboardButton(text=f"ID : {i[0]}                      Ismi : {i[1]}",callback_data=f"{i[0]}")
        ikm.add(button)
    return ikm





