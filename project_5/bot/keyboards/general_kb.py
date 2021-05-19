from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from text.buttons import *
from misc import admin_id

def start_kb(user_id):
    markup = types.InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_gen_new_video, callback_data=btn_gen_new_video), InlineKeyboardButton(text=btn_gen_statistics, callback_data=btn_gen_statistics))
    if user_id == admin_id:
        markup.add(InlineKeyboardButton(text=btn_gen_send_csv, callback_data=btn_gen_send_csv))
    return markup

def send_csv_kb():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_csv_sheets, callback_data=btn_csv_sheets), InlineKeyboardButton(text=btn_csv_excel, callback_data=btn_csv_excel))
    return markup

def have_csv_kb():
    markup = types.InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_have_csv_ok, callback_data=btn_have_csv_ok_data))
    return markup