from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from text.buttons import *

def statistic_kb():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_stat_corr, callback_data=btn_stat_corr), InlineKeyboardButton(text=btn_stat_ttest, callback_data=btn_stat_ttest))
    markup.add(InlineKeyboardButton(text=btn_stat_clean, callback_data=btn_stat_clean))
    return markup

def corr_kb():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_corr_ok, callback_data=btn_corr_ok_data))
    return markup

def ttest_kb():
    markup = types.InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_ttest_ok, callback_data=btn_ttest_ok_data))
    return markup

def clean_kb():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_clean_all, callback_data=btn_clean_all), InlineKeyboardButton(text=btn_clean_last, callback_data=btn_clean_last))
    return markup

def clean_all_kb():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=btn_clean_all_yes, callback_data=btn_clean_all_yes))
    return markup