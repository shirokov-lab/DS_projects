from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.exceptions import *
from misc import dp, bot
from functions.db_sesh import EditDB
from functions.correlation_analysis import corr
from functions.ttest import ttest_get_params
from keyboards.statistics_kb import *
from keyboards.general_kb import *
from text.messages import *
from text.buttons import *

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_gen_statistics)
async def callback_gen_statistics(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == None:
        param_dict = {'status': 'statistics'}
        try:
            await bot.edit_message_text(mes_statistics(db.sesh().count), callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML, reply_markup=statistic_kb())
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_statistics(db.sesh().count), parse_mode=ParseMode.HTML, reply_markup=statistic_kb())
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_stat_corr)
async def callback_stat_corr(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'statistics':
        param_dict = {'status': 'corr_analys', 'message_id_2': db.sesh().message_id}
        try:
            await bot.edit_message_text(mes_corr, callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML)
        except MessageCantBeEdited:
            mes_2 = await bot.send_message(callback_query.from_user.id, mes_corr, parse_mode=ParseMode.HTML)
            param_dict['message_id_2'] = mes_2.message_id
        mes = await bot.send_message(callback_query.from_user.id, corr(db.sesh().id), parse_mode=ParseMode.HTML, reply_markup=corr_kb())
        param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_corr_ok_data)
async def callback_corr_ok(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'corr_analys':
        param_dict = {'status': None, 'message_id_2': None}
        try:
            await bot.delete_message(callback_query.from_user.id, db.sesh().message_id_2)
        except MessageCantBeDeleted: pass
        try:
            await bot.edit_message_text(mes_start(callback_query.from_user.mention), callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_start(callback_query.from_user.mention), parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_stat_ttest)
async def callback_stat_ttest(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'statistics':
        t_test = ttest_get_params(db.sesh().id)
        if t_test != '<b></b>.':
            try:
                await bot.delete_message(callback_query.from_user.id, db.sesh().message_id)
            except MessageCantBeDeleted: pass
            mes = await bot.send_document(callback_query.from_user.id, open('img/img.jpg', 'rb'), caption=mes_ttest+t_test, parse_mode=ParseMode.HTML, reply_markup=ttest_kb())
            param_dict = {'status': 'ttest', 'message_id': mes.message_id}
        else:
            param_dict = {'status': None}
            try:
                await bot.edit_message_text(mes_ttest+mes_ttest_none, callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
            except MessageCantBeEdited:
                mes = await bot.send_message(callback_query.from_user.id, mes_ttest+mes_ttest_none, parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
                param_dict['message_id'] = mes.message_id
        try:
            db.edit_user(param_dict)
        except: pass

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_ttest_ok_data)
async def callback_ttest_ok(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'ttest':
        try:
            await bot.delete_message(callback_query.from_user.id, db.sesh().message_id)
        except MessageCantBeDeleted: pass
        mes = await bot.send_message(callback_query.from_user.id, mes_start(callback_query.from_user.mention), parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
        db.edit_user({'status': None, 'message_id': mes.message_id})

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_stat_clean)
async def callback_stat_clean(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'statistics':
        param_dict = {'status': 'clean_data'}
        try:
            await bot.edit_message_text(mes_clean, callback_query.from_user.id, db.sesh().message_id, reply_markup=clean_kb())
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_clean, reply_markup=clean_kb())
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_clean_all)
async def callback_clean_all(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'clean_data':
        param_dict = {'status': 'clean_all'}
        try:
            await bot.edit_message_text(mes_clean_all, callback_query.from_user.id, db.sesh().message_id, reply_markup=clean_all_kb())
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_clean_all, reply_markup=clean_all_kb())
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_clean_last)
async def callback_clean_last(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'clean_data':
        param_dict = {'status': None}
        try:
            await bot.edit_message_text(mes_clean_last, callback_query.from_user.id, db.sesh().message_id, reply_markup=start_kb(callback_query.from_user.id))
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_clean_last, reply_markup=start_kb(callback_query.from_user.id))
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)
        db.del_observ('last')

@dp.callback_query_handler(lambda callback_query: callback_query.data == btn_clean_all_yes)
async def callback_clean_all_yes(callback_query: types.CallbackQuery):
    db = EditDB(callback_query)
    if db.sesh().status == 'clean_all':
        param_dict = {'status': None}
        try:
            await bot.edit_message_text(mes_start(callback_query.from_user.mention), callback_query.from_user.id, db.sesh().message_id, parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
        except MessageCantBeEdited:
            mes = await bot.send_message(callback_query.from_user.id, mes_start(callback_query.from_user.id), parse_mode=ParseMode.HTML, reply_markup=start_kb(callback_query.from_user.id))
            param_dict['message_id'] = mes.message_id
        db.edit_user(param_dict)
        db.del_observ('all')