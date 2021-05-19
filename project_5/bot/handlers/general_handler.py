from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.exceptions import *
from misc import dp, bot
from functions.db_sesh import EditDB
from functions.send_csv import send_csv
from keyboards.general_kb import *
from text.messages import *
from text.buttons import *

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    if message.chat.type == 'private':
        try:
            await bot.delete_message(message.from_user.id, message.message_id)
        except: pass
        db = EditDB(message)
        param_dict = {'status': None}
        if db.sesh() != None:
            if db.sesh().message_id_2 != None:
                try:
                    await bot.delete_message(message.from_user.id, db.sesh().message_id_2)
                except MessageCantBeEdited: pass
                param_dict['message_id_2'] = None
            try:
                await bot.delete_message(message.from_user.id, db.sesh().message_id)
            except MessageCantBeDeleted: pass
        elif db.sesh() == None:
            db.add_new_user()
        mes = await bot.send_message(message.from_user.id, mes_start(message.from_user.mention), parse_mode=ParseMode.HTML, reply_markup=start_kb(message.from_user.id))
        param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_gen_send_csv)
async def callback_gen_send_csv(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == None:
        param_dict = {'status': 'send_csv'}
        try:
            await bot.edit_message_text(mes_send_csv, callback_query.from_user.id, db.sesh().message_id, reply_markup=send_csv_kb())
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_send_csv, reply_markup=send_csv_kb())
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data in [btn_csv_sheets, btn_csv_excel])
async def callback_csv_program(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'send_csv':
        try:
            await bot.delete_message(callback_query.from_user.id, db.sesh().message_id)
        except MessageCantBeDeleted: pass
        mes = await bot.send_document(callback_query.from_user.id, send_csv(callback_query.data), reply_markup=have_csv_kb())
        db.edit_user({'status': 'have_csv', 'message_id': mes.message_id})

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_have_csv_ok_data)
async def callback_have_csv_ok(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'have_csv':
        try:
            await bot.delete_message(callback_query.from_user.id, db.sesh().message_id)
        except MessageCantBeDeleted: pass
        mes = await bot.send_message(callback_query.from_user.id, mes_start(callback_query.from_user.mention), parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
        db.edit_user({'status': None, 'message_id': mes.message_id})