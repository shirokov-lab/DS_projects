from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from text.buttons import *

def quest_kb(status):
    markup = types.InlineKeyboardMarkup()
    if status == 'quest_4':
        markup.add(InlineKeyboardButton(text=quest_5_btn_1, callback_data=quest_5_btn_1))
        markup.add(InlineKeyboardButton(text=quest_5_btn_2, callback_data=quest_5_btn_2))
    elif status == 'quest_5':
        markup.add(InlineKeyboardButton(text=quest_6_btn_1, callback_data=quest_6_btn_1), InlineKeyboardButton(text=quest_6_btn_2, callback_data=quest_6_btn_2), InlineKeyboardButton(text=quest_6_btn_3, callback_data=quest_6_btn_3))
        markup.add(InlineKeyboardButton(text=quest_6_btn_4, callback_data=quest_6_btn_4), InlineKeyboardButton(text=quest_6_btn_5, callback_data=quest_6_btn_5), InlineKeyboardButton(text=quest_6_btn_6, callback_data=quest_6_btn_6))
        markup.add(InlineKeyboardButton(text=quest_6_btn_7, callback_data=quest_6_btn_7), InlineKeyboardButton(text=quest_6_btn_8, callback_data=quest_6_btn_8), InlineKeyboardButton(text=quest_6_btn_9, callback_data=quest_6_btn_9))
        markup.add(InlineKeyboardButton(text=quest_6_btn_10, callback_data=quest_6_btn_10_data))
    elif status == 'quest_6':
        markup.add(InlineKeyboardButton(text=quest_7_btn_1, callback_data=quest_7_btn_1), InlineKeyboardButton(text=quest_7_btn_2, callback_data=quest_7_btn_2), InlineKeyboardButton(text=quest_7_btn_3, callback_data=quest_7_btn_3))
        markup.add(InlineKeyboardButton(text=quest_7_btn_4, callback_data=quest_7_btn_4), InlineKeyboardButton(text=quest_7_btn_5, callback_data=quest_7_btn_5), InlineKeyboardButton(text=quest_7_btn_6, callback_data=quest_7_btn_6))
        markup.add(InlineKeyboardButton(text=quest_7_btn_7, callback_data=quest_7_btn_7), InlineKeyboardButton(text=quest_7_btn_8, callback_data=quest_7_btn_8), InlineKeyboardButton(text=quest_7_btn_9, callback_data=quest_7_btn_9))
        markup.add(InlineKeyboardButton(text=quest_7_btn_10, callback_data=quest_7_btn_10), InlineKeyboardButton(text=quest_7_btn_11, callback_data=quest_7_btn_11))
    elif status == 'quest_7':
        markup.add(InlineKeyboardButton(text=quest_8_btn_1, callback_data=quest_8_btn_1), InlineKeyboardButton(text=quest_8_btn_2, callback_data=quest_8_btn_2))
        markup.add(InlineKeyboardButton(text=quest_8_btn_3, callback_data=quest_8_btn_3), InlineKeyboardButton(text=quest_8_btn_4, callback_data=quest_8_btn_4))
    elif status == 'quest_8':
        markup.add(InlineKeyboardButton(text=quest_9_btn_1, callback_data=quest_9_btn_1), InlineKeyboardButton(text=quest_9_btn_2, callback_data=quest_9_btn_2))
        markup.add(InlineKeyboardButton(text=quest_9_btn_3, callback_data=quest_9_btn_3))
        markup.add(InlineKeyboardButton(text=quest_9_btn_4, callback_data=quest_9_btn_4_data), InlineKeyboardButton(text=quest_9_btn_5, callback_data=quest_9_btn_5))
    elif status == 'quest_9':
        markup.add(InlineKeyboardButton(text=quest_10_btn_1, callback_data=quest_10_btn_1), InlineKeyboardButton(text=quest_10_btn_2, callback_data=quest_10_btn_2))
        markup.add(InlineKeyboardButton(text=quest_10_btn_3, callback_data=quest_10_btn_3), InlineKeyboardButton(text=quest_10_btn_4, callback_data=quest_10_btn_4))
    elif status == 'quest_10':
        markup.add(InlineKeyboardButton(text=quest_11_btn_1, callback_data=quest_11_btn_1_data), InlineKeyboardButton(text=quest_11_btn_2, callback_data=quest_11_btn_2_data))
    elif status == 'quest_11':
        markup.add(InlineKeyboardButton(text=quest_12_btn_1, callback_data=quest_12_btn_1_data), InlineKeyboardButton(text=quest_12_btn_2, callback_data=quest_12_btn_2_data))
    elif status == 'quest_12':
        markup.add(InlineKeyboardButton(text=quest_13_btn_1, callback_data=quest_13_btn_1_data), InlineKeyboardButton(text=quest_13_btn_2, callback_data=quest_13_btn_2_data))
    elif status == 'quest_13':
        markup.add(InlineKeyboardButton(text=quest_14_btn_1, callback_data=quest_14_btn_1), InlineKeyboardButton(text=quest_14_btn_2, callback_data=quest_14_btn_2))
    elif status == 'quest_14':
        markup.add(InlineKeyboardButton(text=quest_15_btn_1, callback_data=quest_15_btn_1_data), InlineKeyboardButton(text=quest_15_btn_2, callback_data=quest_15_btn_2_data))
    elif status == 'quest_15':
        markup.add(InlineKeyboardButton(text=quest_16_btn_1, callback_data=quest_16_btn_1), InlineKeyboardButton(text=quest_16_btn_2, callback_data=quest_16_btn_2))
        markup.add(InlineKeyboardButton(text=quest_16_btn_3, callback_data=quest_16_btn_3), InlineKeyboardButton(text=quest_16_btn_4, callback_data=quest_16_btn_4))
        markup.add(InlineKeyboardButton(text=quest_16_btn_5, callback_data=quest_16_btn_5))
    elif status == 'quest_16':
        markup.add(InlineKeyboardButton(text=quest_17_btn_1, callback_data=quest_17_btn_1_data), InlineKeyboardButton(text=quest_17_btn_2, callback_data=quest_17_btn_2_data))
    elif status == 'quest_17':
        markup.add(InlineKeyboardButton(text=quest_18_btn_1, callback_data=quest_18_btn_1_data), InlineKeyboardButton(text=quest_18_btn_2, callback_data=quest_18_btn_2_data))
    elif status == 'quest_18':
        markup.add(InlineKeyboardButton(text=quest_19_btn_1, callback_data=quest_19_btn_1_data), InlineKeyboardButton(text=quest_19_btn_2, callback_data=quest_19_btn_2_data))
    elif status == 'quest_19':
        markup.add(InlineKeyboardButton(text=quest_20_btn_1, callback_data=quest_20_btn_1), InlineKeyboardButton(text=quest_20_btn_2, callback_data=quest_20_btn_2))
        markup.add(InlineKeyboardButton(text=quest_20_btn_3, callback_data=quest_20_btn_3_data))
    elif status == 'quest_20':
        markup.add(InlineKeyboardButton(text=quest_21_btn_1, callback_data=quest_21_btn_1_data), InlineKeyboardButton(text=quest_21_btn_2, callback_data=quest_21_btn_2_data))
    elif status == 'quest_21':
        markup.add(InlineKeyboardButton(text=quest_22_btn_1, callback_data=quest_22_btn_1))
        markup.add(InlineKeyboardButton(text=quest_22_btn_2, callback_data=quest_22_btn_2))
        markup.add(InlineKeyboardButton(text=quest_22_btn_3, callback_data=quest_22_btn_3))
    return markup