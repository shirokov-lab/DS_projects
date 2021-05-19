from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.exceptions import *
from misc import dp, bot
from functions.db_sesh import EditDB
from text.messages import *
from text.buttons import *
from keyboards.general_kb import *
from keyboards.interview_kb import *

'''START - QUEST 1'''
@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_gen_new_video)
async def callback_gen_new_video(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == None:
        param_dict = {'status': 'quest_1'}
        try:
            await bot.edit_message_text(mes_quest_1, callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML)
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_quest_1, parse_mode=ParseMode.HTML)
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

'''QUEST 1 - QUEST 5'''
@dp.message_handler(content_types=['text'])
async def answer_quests_1_4(message: types.Message):
    if message.chat.type == 'private':
        await bot.delete_message(message.from_user.id, message.message_id)
        db = EditDB(message)
        try:
            answer = int(message.text)
            markup = None
            quest = 'question_'
            next_door = False
            if db.sesh().status == 'quest_1':
                mes_text = mes_quest_2
                quest += '1'
                n = '2'
                next_door = True
            elif db.sesh().status == 'quest_2':
                mes_text = mes_quest_3
                quest += '2'
                n = '3'
                next_door = True
            elif db.sesh().status == 'quest_3':
                mes_text = mes_quest_4
                quest += '3'
                n = '4'
                next_door = True
            elif db.sesh().status == 'quest_4':
                mes_text = mes_quest_5
                quest += '4'
                n = '5'
                next_door = True
                markup = quest_kb(db.sesh().status)
            if next_door == True:
                param_dict = {'status': db.sesh().status[:6]+n, quest: answer}
                try:
                    await bot.edit_message_text(mes_text, message.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML, reply_markup=markup)
                except MessageCantBeEdited:
                    mes = await bot.send_message(message.from_user.id, mes_text, parse_mode=ParseMode.HTML, reply_markup=markup)
                    param_dict['message_id'] = mes.message_id
                db.edit_user(param_dict)
        except ValueError: pass

@dp.callback_query_handler(lambda callback_query: callback_query.data in interview_btns)
async def answer_quests_5_end(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    markup = quest_kb(db.sesh().status)
    quest = 'question_'
    next_door = False
    status = db.sesh().status[:6]
    end_inter = False
    if (db.sesh().status == 'quest_5') and (callback_query.data in quest_5_btns):
        mes_text = mes_quest_6
        quest += '5'
        status += '6'
        next_door = True
    elif (db.sesh().status == 'quest_6') and (callback_query.data in quest_6_btns):
        mes_text = mes_quest_7
        quest += '6'
        status += '7'
        next_door = True
    elif (db.sesh().status == 'quest_7') and (callback_query.data in quest_7_btns):
        mes_text = mes_quest_8
        quest += '7'
        status += '8'
        next_door = True
    elif (db.sesh().status == 'quest_8') and (callback_query.data in quest_8_btns):
        mes_text = mes_quest_9
        quest += '8'
        status += '9'
        next_door = True
    elif (db.sesh().status == 'quest_9') and (callback_query.data in quest_9_btns):
        mes_text = mes_quest_10
        quest += '9'
        status += '10'
        next_door = True
    elif (db.sesh().status == 'quest_10') and (callback_query.data in quest_10_btns):
        mes_text = mes_quest_11
        quest += '10'
        status += '11'
        next_door = True
    elif (db.sesh().status == 'quest_11') and (callback_query.data in quest_11_btns):
        mes_text = mes_quest_12
        quest += '11'
        status += '12'
        next_door = True
    elif (db.sesh().status == 'quest_12') and (callback_query.data in quest_12_btns):
        mes_text = mes_quest_13
        quest += '12'
        status += '13'
        next_door = True
    elif (db.sesh().status == 'quest_13') and (callback_query.data in quest_13_btns):
        mes_text = mes_quest_14
        quest += '13'
        status += '14'
        next_door = True
    elif (db.sesh().status == 'quest_14') and (callback_query.data in quest_14_btns):
        mes_text = mes_quest_15
        quest += '14'
        status += '15'
        next_door = True
    elif (db.sesh().status == 'quest_15') and (callback_query.data in quest_15_btns):
        mes_text = mes_quest_16
        quest += '15'
        status += '16'
        next_door = True
    elif (db.sesh().status == 'quest_16') and (callback_query.data in quest_16_btns):
        mes_text = mes_quest_17
        quest += '16'
        status += '17'
        next_door = True
    elif (db.sesh().status == 'quest_17') and (callback_query.data in quest_17_btns):
        mes_text = mes_quest_18
        quest += '17'
        status += '18'
        next_door = True
    elif (db.sesh().status == 'quest_18') and (callback_query.data in quest_18_btns):
        mes_text = mes_quest_19
        quest += '18'
        status += '19'
        next_door = True
    elif (db.sesh().status == 'quest_19') and (callback_query.data in quest_19_btns):
        mes_text = mes_quest_20
        quest += '19'
        status += '20'
        next_door = True
    elif (db.sesh().status == 'quest_20') and (callback_query.data in quest_20_btns):
        mes_text = mes_quest_21
        quest += '20'
        status += '21'
        next_door = True
    elif (db.sesh().status == 'quest_21') and (callback_query.data in quest_21_btns):
        mes_text = mes_quest_22
        quest += '21'
        status += '22'
        next_door = True
    elif (db.sesh().status == 'quest_22') and (callback_query.data in quest_22_btns):
        mes_text = mes_end_questions
        quest += '22'
        status = None
        next_door = True
        end_inter = True
        markup = start_kb(callback_query.from_user.id)
    if next_door == True:
        param_dict = {'status': status, quest: callback_query.data.replace(db.sesh().status[5:], '')}
        try:
            await bot.edit_message_text(mes_text, callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML, reply_markup=markup)
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_text, parse_mode=ParseMode.HTML, reply_markup=markup)
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)
        if end_inter == True:
            db.add_observ()