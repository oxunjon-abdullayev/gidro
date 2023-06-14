
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def user_rkm() -> ReplyKeyboardMarkup:
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="👥 Fuqarolar")
    rkm.add(button)
    return rkm




def cancel_back() :
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="cancel")
    rkm.add(button)
    return rkm



def back_to_home() :
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="⬅️orqaga qaytish")
    rkm.add(button)
    return rkm




def ortga_qaytish() :
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="✅ orqaga qaytish")
    rkm.add(button)
    return rkm


def user_panel_default_button():
   rkm = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
   btn1=KeyboardButton(text="✅ Ro'yxatdan o'tish")
   btn2=KeyboardButton(text="☎ Bizning aloqa manzil")
   btn3=KeyboardButton(text="📍 Bizning manzil")
   rkm.add(btn1,btn2,btn3)
   return rkm



def user_location():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("📍 locatsiya", request_location=True)
    rkm.add(btn)
    return rkm


