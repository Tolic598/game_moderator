from multiprocessing import context
from shutil import ignore_patterns
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Dispatcher, types
from numpy import equal
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
import pymysql
from pymysql.cursors import DictCursor
import pymysql.cursors
import datetime, time
from aiogram.types import CallbackQuery
from keyboards import kbadmin, kbpt, kbadmin_chat
from config import host, user, password, db_name

try:
    connection = pymysql.connect(host = host,
                                user = user,
                                password = password,
                                database = db_name,
                                charset='utf8mb4',
                                port=3306,
                                cursorclass=DictCursor)
    print("ок")
except Exception as ex:
    print(ex)


class FSMadmin(StatesGroup):
    text = State()
    photo = State()
    text1 = State()
    
    text_ls = State()
    photo_ls = State()
    text_ls_photo = State()
    
    text_chat = State()
    text_chat_photo = State()
    text_chat_photo_ls = State()

'''#''''''''''''''''''''''''''''''''''''''''Запуск админки всем админам''''''''''''''''''''''''''''''''''''''''''''#'''
async def admin(message: types.Message):
    id = message.from_user.id
    names=message.from_user.first_name
    if id == 2116070853:
        await bot.send_message(id, "Вы зашли в админку",reply_markup=kbadmin)
    else:
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT * FROM chat WHERE id={id}")
            for row in cursors:
                idi = row['id']
                if str(id) == str(idi):
                    await bot.send_message(id, "Вы зашли в админку",reply_markup=kbadmin_chat)
        connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''Запуск cмены приветствия''''''''''''''''''''''''''''''''''''''''''''#'''
async def greetings_chat(call: CallbackQuery):
    id = call.from_user.id
    await FSMadmin.text_chat.set()
    await call.message.answer("Введите новое приветствие для пользователя\nвы можете использовать тригеры:\n{name} - имя\n{username} - юзернейм")
    
'''#''''''''''''''''''''''''''''''''''''''''cмены приветствия''''''''''''''''''''''''''''''''''''''''''''#'''
async def ras_chat_chat(message: types.Message, state: FSMadmin):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    async with state.proxy() as data:
        data['text_chat'] = message.text
    async with state.proxy() as data:
        text_chat = data['text_chat']
        sample_text1 = text_chat
        t1 = sample_text1.replace('{name}', f'{name}')
        t2 = t1.replace('{username}', f'{username}')
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT * FROM chat WHERE id={id}")
            if text_chat == "отмена" or text_chat == "Отмена":
                current_state = await state.get_state()
                if current_state is None:
                    return
                await state.finish()
                await message.reply("ок",reply_markup=kbadmin_chat)
            else:
                cursors.execute("UPDATE chat SET greetings=%s WHERE id=%s",(t2,id))
                await bot.send_message(id, f"✅Вы успешно задали приветствие: {t2}",reply_markup=kbadmin_chat)
                await state.finish()
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''cмены приветствия + фото''''''''''''''''''''''''''''''''''''''''''''#'''
async def greetings_chat_photo(call: CallbackQuery):
    id = call.from_user.id
    await FSMadmin.text_chat_photo.set()
    await call.message.answer(f"Загрузи фото для приветствия пользователя:\n")
    
async def greetings_chat_photo_ls(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['text_chat_photo'] = message.photo[0].file_id
    await FSMadmin.next()
    await bot.send_message(id,"Фото принято теперь отправьте текст\nвы можете использовать тригеры:\n{name} - имя\n{username} - юзернейм:")
    
async def greetings_chat_photo_ls_p(message: types.Message, state: FSMContext):
    id = message.from_user.id
    name = message.from_user.first_name
    username = message.from_user.username
    async with state.proxy() as data:
        data['text_chat_photo_ls'] = message.text
    async with state.proxy() as data:
        img = data['text_chat_photo']
        text1 = data['text_chat_photo_ls']
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT chat_id FROM chat")
            t1 = text1.replace('{name}', f'{name}')
            t2 = t1.replace('{username}', f'{username}')
            if text1 == "отмена" or text1 == "Отмена":
                current_state = await state.get_state()
                if current_state is None:
                    return
                await state.finish()
                await message.reply("ок",reply_markup=kbadmin_chat)
            else:
                cursors.execute("UPDATE chat SET greetings=%s WHERE id=%s",(t2,id))
                cursors.execute("UPDATE chat SET img=%s WHERE id=%s",(img,id))
                await bot.send_photo(id, img, caption = f'✅Вы успешно задали приветствие: {t2}',reply_markup=kbadmin_chat)
                await state.finish()
        connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''текущее приветствие''''''''''''''''''''''''''''''''''''''''''''#'''
async def greetings_chat_t(call: CallbackQuery):
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM chat WHERE id={id}")
        for row in cursors:
            greetings = row['greetings']
            img = row['img']
            if img == "":
                await call.message.answer(f"Текущее приветствие:\n{greetings}\n",reply_markup=kbadmin_chat)
            else:
                await bot.send_photo(id, img, caption = f'Текущее приветствие:\n{greetings}',reply_markup=kbadmin_chat)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''рассылка  в личку''''''''''''''''''''''''''''''''''''''''''''#'''
async def ras_chat(call: CallbackQuery):
    id = call.from_user.id
    await FSMadmin.text.set()
    await call.answer(f"Введите текст для расссылки всем пользователям:\n")
    
async def ras_chat1(message: types.Message, state: FSMadmin):
    id = message.from_user.id
    async with state.proxy() as data:
        data['text'] = message.text
    async with state.proxy() as data:
        text_chat = data['text']
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT id FROM user")
            if text_chat == "отмена" or text_chat == "Отмена":
                current_state = await state.get_state()
                if current_state is None:
                    return
                await state.finish()
                await message.reply("ок",reply_markup=kbadmin)
            else:
                await bot.send_message(id, "отправка сообщения....")
                try:
                    for row in cursors:
                        chat_idi = row['id']
                        await bot.send_message(chat_idi, text_chat)
                except Exception as pocinul:
                    await bot.send_message(id, f"❎рассылка не отправлена,пользователь не активен:\n{pocinul}\n")
                await bot.send_message(id, "✅рассылка закончена✅",reply_markup=kbadmin)
                await state.finish()
        connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''рассылка  с фото''''''''''''''''''''''''''''''''''''''''''''#'''
async def ras_chat_photo(call: CallbackQuery):
    id = call.from_user.id
    await FSMadmin.photo.set()
    await call.answer(f"Загрузи фото:\n")

async def load_photo(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMadmin.next()
    await bot.send_message(id,"Фото принято теперь отправьте текст:")
    
async def load_photo_text(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['text1'] = message.text
    async with state.proxy() as data:
        photo = data['photo']
        text1 = data['text1']
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT id FROM user")
            await bot.send_message(id, "отправка сообщения....")
            try:
                for row in cursors:
                    chat_idi = row['id']
                    await bot.send_photo(chat_idi, photo, caption = f'{text1}')
            except Exception as pocinul:
                await bot.send_message(id, f"❎рассылка не отправлена,пользователь не активен:\n{pocinul}\n")
            await bot.send_message(id, "✅рассылка закончена✅",reply_markup=kbadmin)
            await state.finish()
        connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''рассылка  в чат''''''''''''''''''''''''''''''''''''''''''''#'''
async def ras_chat_ls(call: CallbackQuery):
    id = call.from_user.id
    await FSMadmin.text_ls.set()
    await call.answer(f"Введите текст для расссылки в чате:\n")
    
async def ras_chat1_ls(message: types.Message, state: FSMadmin):
    id = message.from_user.id
    async with state.proxy() as data:
        data['text_ls'] = message.text
    async with state.proxy() as data:
        text_chat = data['text_ls']
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT chat_id FROM chat")
            if text_chat == "отмена" or text_chat == "Отмена":
                current_state = await state.get_state()
                if current_state is None:
                    return
                await state.finish()
                await message.reply("ок",reply_markup=kbadmin)
            else:
                await bot.send_message(id, "отправка сообщения....")
                for row in cursors:
                    chat_idi = row['chat_id']
                    await bot.send_message(chat_idi, text_chat)
                await bot.send_message(id, "✅рассылка закончена✅",reply_markup=kbadmin)
                await state.finish()
        connection.commit()

'''#''''''''''''''''''''''''''''''''''''''''рассылка  в чат + фото''''''''''''''''''''''''''''''''''''''''''''#'''
async def ras_chat_photo_ls(call: CallbackQuery):
    id = call.from_user.id
    await FSMadmin.photo_ls.set()
    await call.answer(f"Загрузи фото:\n")

async def load_photo_ls(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['photo_ls'] = message.photo[0].file_id
    await FSMadmin.next()
    await bot.send_message(id,"Фото принято теперь отправьте текст:")
    
async def load_photo_text_ls(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['text_ls_photo'] = message.text
    async with state.proxy() as data:
        photo = data['photo_ls']
        text1 = data['text_ls_photo']
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT chat_id FROM chat")
            await bot.send_message(id, "отправка сообщения....")
            try:
                for row in cursors:
                    chat_idi = row['chat_id']
                    await bot.send_photo(chat_idi, photo, caption = f'{text1}')
            except Exception as pocinul:
                await bot.send_message(id, f"❎рассылка не отправлена,пользователь не активен:\n{pocinul}\n")
            await bot.send_message(id, "✅рассылка закончена✅",reply_markup=kbadmin)
            await state.finish()
        connection.commit()
        
'''#''''''''''''''''''''''''''''''''''''''''рассылка  отмена''''''''''''''''''''''''''''''''''''''''''''#'''
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("ок")
    

'''#''''''''''''''''''''''''''''''''''''''''регестрация хэндлеров''''''''''''''''''''''''''''''''''''''''''''#'''
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(admin, commands=['admin'])
# '''#''''''''''''''''''''''''''''''''''''''''Запуск cмены приветствия''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(greetings_chat, text="greetings_chat", state=None)
    dp.register_message_handler(ras_chat_chat, state=FSMadmin.text_chat)
# '''#''''''''''''''''''''''''''''''''''''''''Запуск cмены приветствия + фото''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(greetings_chat_photo, text="greetings_chat_photo", state=None)
    dp.register_message_handler(greetings_chat_photo_ls, content_types=['photo'], state=FSMadmin.text_chat_photo)
    dp.register_message_handler(greetings_chat_photo_ls_p, state=FSMadmin.text_chat_photo_ls)
# '''#''''''''''''''''''''''''''''''''''''''''текущее приветствие''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(greetings_chat_t, text="greetings_chat_t")
# '''#''''''''''''''''''''''''''''''''''''''''рассылка  в личку''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(ras_chat, text="ras_chat", state=None)
    dp.register_message_handler(ras_chat1, state=FSMadmin.text)
# '''#''''''''''''''''''''''''''''''''''''''''рассылка  с фото''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(ras_chat_photo, text="ras_chat_photo", state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_photo_text, state=FSMadmin.text1)
# '''#''''''''''''''''''''''''''''''''''''''''рассылка  в чат''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(ras_chat_ls, text="ras_chat_ls", state=None)
    dp.register_message_handler(ras_chat1_ls, state=FSMadmin.text_ls)
# '''#''''''''''''''''''''''''''''''''''''''''рассылка  с фото в чат''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_callback_query_handler(ras_chat_photo_ls, text="ras_chat_photo_ls", state=None)
    dp.register_message_handler(load_photo_ls, content_types=['photo'], state=FSMadmin.photo_ls)
    dp.register_message_handler(load_photo_text_ls, state=FSMadmin.text_ls_photo)
# '''#''''''''''''''''''''''''''''''''''''''''рассылка  отмена''''''''''''''''''''''''''''''''''''''''''''#'''
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")