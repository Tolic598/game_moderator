from matplotlib.pyplot import text
from keyboards import kb, kb1, kb2, kbDice, menu, menuprof, kbsum, kbDic, rest, kbdart, kbdarts, restd, kbbs,  kbbast, restbbs, kbfud, fud, restfud, kbslot, restslot, restbow, kbbowl, kbbow, kbpt, kbpt_art, kbpt_art_pok_1, kbpt_art_pok_2, kbpt_art_pok_3, kbpt_art_pok_4, kbpt_art_pok_5, kbpt_art_pok_6, kbpt_art_pok_7, kbpt_art_pok_8, kbpt_art_pok_9, kbpt_art_pok_10
from multiprocessing import context
from shutil import ignore_patterns
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import BoundFilter
from aiogram import Dispatcher, types
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
import random
from aiogram import types
import pymysql
from pymysql.cursors import DictCursor
import pymysql.cursors
import datetime, time
import random 
from config import host, user, password, db_name
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

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


start_time = time.time()

conversations = {}
infos = {}

dt = datetime.datetime.today().strftime('%d.%m %H:%M')
end_time = (time.time()) - start_time

print((f'Бот запущен\nДата запуска: {dt}\nВремя запуска: {round(end_time,1)} секунды\n'))

class FSMclient(StatesGroup):
    sumD=State()
    sumD2=State()
    sumD3=State()
    sumD4=State()
    sumD5=State()
    sumD6=State()
    
    sumDA=State()
    sumDA1=State()
    sumDA2=State()
    sumDA3=State()
    sumDA4=State()
    
    sumBA=State()
    sumBA1=State()
    sumBA2=State()
    
    sumFO=State()
    sumFO1=State()
    sumFO2=State()
    
    sumSL=State()
    
    sumBO=State()
    sumBO1=State()
    sumBO2=State()

    obm=State()
'''#''''''''''''''''''''''''''''''''''''''''Запуск автоначисления''''''''''''''''''''''''''''''''''''''''''''#'''
async def some_work():
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user")
        for row in cursors:
            id = row['id']
            artef = row['artef']
            balance = row['balance']
            ocup = row['ocup']
            if artef == "Кольцо подавления":
                balance_p = balance + 30
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Кукла шамана":
                balance_p = balance + random.randint(40,65)
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Кулон разорения":
                balance_p = balance + 75
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Подкова демона":
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                balance_p = balance + random.randint(75,100)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Рог бездны":
                balance_p = balance + 130
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Щит морской славы":
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                balance_p = balance + random.randint(130,150)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Сапоги странника":
                balance_p = balance + 180
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Трезубец могущества":
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                balance_p = balance + random.randint(180,200)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Корона пяти морей":
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                balance_p = balance + 250
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            elif artef == "Королевские доспехи":
                cursors.execute("UPDATE user SET ocup=ocup + %s WHERE id=%s",(1,id))
                balance_p = balance + 500
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
            else:
                cursors.execute("UPDATE user SET balance=balance + %s WHERE id=%s",(10,id))
                cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(0,id))
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''Запуск бота''''''''''''''''''''''''''''''''''''''''''''#'''
async def start_bot(message: types.Message):
    id = message.from_user.id
    names=message.from_user.first_name
    username=message.from_user.username
    dates=datetime.datetime.today().strftime('%d.%m %H:%M')
    balance = 100
    cristall = 0
    pop = 0
    viv = 0
    victory = 0
    devence = 0
    col = 0
    levels = 1
    xp = 100
    num = 0
    num1 = 0
    statuss = 0
    status_chat = 0
    artef = "Не куплено"
    ocup = 0
    cvest_po = "0"
    greetings = f"Добро пожаловать {names}, в наш чат"
    img = ""
    chat_id = message.chat.id
    if message.chat.type == "private":
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT * FROM user WHERE id=%s",(id))
            if cursors.rowcount == 1:
                await message.answer(f"👨‍🔧 Главное меню!", reply_markup=menu)
                scheduler.add_job(some_work, 'cron', hour=23, minute=0)
                scheduler.start()
            
            elif cursors.rowcount == 0:
                if id == 5560808383:
                    await message.answer(f"📛Вы забанины,обнаружен купленый номер📛")
                else:
                    cursors.execute('''INSERT IGNORE INTO user(id,names,dates,cristall,balance,pop,viv,victory,devence,col,levels,xp,num,num1,statuss, artef, ocup, cvest_po)
                        VALUES(%d,'%s','%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s','%s')''' % (int(id),names,dates,int(cristall),int(balance),int(pop),int(viv),int(victory),int(devence),int(col),int(levels),int(xp),int(num),int(num1),int(statuss), artef, ocup, cvest_po))
                    await message.answer(f"👨‍🔧 приветствую: {names}!\nЯ могу предложить следующие функции:", reply_markup=menu)
            else:
                bot.send_message(id,"Такой кнопки нет")
        connection.commit()
    else:
        chat = await bot.get_chat_member(message.chat.id, 5018144842)
        if chat.status == 'administrator':
            chat_admin = await bot.get_chat_member(message.chat.id, id)
            if chat_admin.status == 'creator':
                admin_user = chat_admin.user.username
                chat_name = message.chat.title
                chat_user = message.chat.username
                textx = ""
                descriptions = "администрация не задала описание"
                id = message.from_user.id
                with connection.cursor() as cursors:
                    cursors.execute(f"SELECT * FROM chat WHERE chat_id={chat_id}")
                    if cursors.rowcount == 1:
                        await message.answer(f"👨‍🔧 Главное меню!", reply_markup=menu)
                    
                    elif cursors.rowcount == 0:
                        cursors.execute('''INSERT IGNORE INTO chat(id,chat_id,admin_user,chat_name,chat_user,descriptions, textx,status_chat, greetings, img)
                            VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (id,chat_id,admin_user,chat_name,chat_user,descriptions, textx, status_chat, greetings, img))
                        await message.answer(f"👨‍🔧 Главное меню!", reply_markup=menu)
                        
                connection.commit()
                        
                with connection.cursor() as cursors:
                        cursors.execute(f"SELECT * FROM user WHERE id=%s",(id))
                        if cursors.rowcount == 1:
                            pass
                        
                        elif cursors.rowcount == 0:
                            cursors.execute('''INSERT IGNORE INTO user(id,names,dates,cristall,balance,pop,viv,victory,devence,col,levels,xp,num,num1,statuss, artef, ocup, cvest_po)
                        VALUES(%d,'%s','%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s','%s')''' % (int(id),names,dates,int(cristall),int(balance),int(pop),int(viv),int(victory),int(devence),int(col),int(levels),int(xp),int(num),int(num1),int(statuss), artef, ocup, cvest_po))
                connection.commit()
            else:
                with connection.cursor() as cursors:
                    cursors.execute(f"SELECT * FROM user WHERE id={id}")
                    if cursors.rowcount == 1:
                        await message.answer(f"👨‍🔧 Главное меню!", reply_markup=menu)
                    
                    elif cursors.rowcount == 0:
                        cursors.execute('''INSERT IGNORE INTO user(id,names,dates,cristall,balance,pop,viv,victory,devence,col,levels,xp,num,num1,statuss, artef, ocup, cvest_po)
                        VALUES(%d,'%s','%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s','%s')''' % (int(id),names,dates,int(cristall),int(balance),int(pop),int(viv),int(victory),int(devence),int(col),int(levels),int(xp),int(num),int(num1),int(statuss), artef, ocup, cvest_po))
                        await message.answer(f"👨‍🔧 приветствую: {names}!\nЯ могу предложить следующие функции:", reply_markup=menu)
                        
                connection.commit()
        else:
            await message.answer(f"👨‍🔧  Бот не являеться администратором\n✅ Установка Game | Чат-менеджера довольно проста:\n\n1) Нажмите на название СВОЕГО чата, после на карандаш сверху;\n2) Перейдите в пункт «Администраторы»;\n3) Нажмите на кнопку «Добавить администратора»;\n4) Выберите из списка «@moderatorchatIbot»")
            
'''#''''''''''''''''''''''''''''''''''''''''🗣️Информация📃''''''''''''''''''''''''''''''''''''''''''''#'''
async def Info(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    await call.message.answer(f"📃Вас приветствует Game | Чат-менеджер, бот может предоставить следующие функции:\n1)📜Квест📜\n2)🔮Артефакты🔮 \n3)🎮Игры 🎮\n \n 🗣️Подробней о квестах: \n Раз в сутки вам доступен квест в котором можно заработать от  15 до 100   Gamecoin, а также можно потерять 15 Gamecoin \n \n 🗣️Подробней о артефактах: \n Артефакты нужны для вывода Gamecristall, а также для пассивного заработка каждых 24 часа \n \n 🗣️Подробней о играх:  \n В боте присутствуют 6 игр, каждая из них может как принести вам  Gamecoin, также их и забрать\n \n 🪧Бот запущен: {dt}\n🪪Администрация: @codetolic", reply_markup=menu)

'''#''''''''''''''''''''''''''''''''''''''''приветствия нового пользователя в чате''''''''''''''''''''''''''''''''''''''''''''#'''
async def greetings(message: types.Message):
    name=message.from_user.first_name
    famili=message.from_user.last_name
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM chat")
        for row in cursors:
            greetings = row['greetings']
            chat_id = row['chat_id']
            img = row['img']
            if img == "":
                await bot.send_message(chat_id, f"{greetings}")
            else:
                await bot.send_photo(chat_id, img, caption = f'{greetings}')
    connection.commit()

'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн''''''''''''''''''''''''''''''''''''''''''''#'''
async def Menu(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    names=call.from_user.first_name
    username=call.from_user.username
    await call.message.answer(f"👨‍🔧 Главное меню!", reply_markup=menu)
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  игры''''''''''''''''''''''''''''''''''''''''''''#'''
async def Game(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    names=call.from_user.first_name
    username=call.from_user.username
    msg = await call.message.answer(f"Наши игры:", reply_markup=kb)
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  профиль''''''''''''''''''''''''''''''''''''''''''''#'''
async def Prof(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    names=call.from_user.first_name
    username=call.from_user.username
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            dates = row['dates']
            balance = row['balance']
            cristall = row['cristall']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            xp = row['xp']
            artef = row['artef']
            await call.message.answer(f"Профиль игрока {names}:\nID: {id}\nЮзер: @{username}\nGamecoin: {balance}\nGamecristall: {cristall}\nАртефакты:{artef}\nПобед: {victory}\nПроиграшей: {devence}\nИгр сыграно: {col}\nЖизнь: {xp}\nВремя регестрации: {dates}", reply_markup=menuprof)
    connection.commit()
    
async def pop(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    await call.message.answer(f"В разработке", reply_markup=menuprof)
    
async def viv(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    await call.message.answer(f"В разработке", reply_markup=menuprof)
        
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  профиль обменик''''''''''''''''''''''''''''''''''''''''''''#'''
async def obmen(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            cristall = row['cristall']
            if balance >= 1000:
                await FSMclient.obm.set()
                await call.message.answer(f"🗣️Введите сумму для обмена Gamecoin на Gamecristall\n💰Текущий баланс Gamecoin: {balance}\n🛑Минимальный обмен от 1000 Gamecoin\n↪️Текущий курс обмена 1000 Gamecoin = 10 Gamecristall↩️")
            else:
                await call.message.answer(f"🛑Минимальный обмен от 1000 Gamecoin🛑\n💰Текущий баланс Gamecoin: {balance}", reply_markup=menuprof)
    connection.commit()
    
async def obmen_game(message: types.Message, state: FSMclient):
    id = message.from_user.id
    async with state.proxy() as data:
        data['obm'] = message.text
    async with state.proxy() as data:
        obm = data['obm']
        with connection.cursor() as cursors:
            cursors.execute(f"SELECT * FROM user WHERE id={id}")
            if int(obm) >= 1000:
                if obm == "отмена" or obm == "Отмена":
                    current_state = await state.get_state()
                    if current_state is None:
                        return
                    await state.finish()
                    await message.reply("ок",reply_markup=menuprof)
                else:
                    obm_cristall = int(obm) / int(100)
                    cursors.execute("UPDATE user SET balance=balance - %s WHERE id=%s",(obm,id))
                    cursors.execute("UPDATE user SET cristall=cristall + %s WHERE id=%s",(obm_cristall,id))
                    await bot.send_message(id, f"✅Вы успешно обменяли {obm} Gamecoin на {obm_cristall} Gamecristall", reply_markup=menuprof)
                    await state.finish()
            else:
                await bot.send_message(id, f"🛑Минимальный обмен от 1000 Gamecoin🛑", reply_markup=menuprof)
                await state.finish()
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн квест''''''''''''''''''''''''''''''''''''''''''''#'''
async def cvest(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            cvest_po = row['cvest_po']
            if cvest_po == "0":
                coint = random.randint(1,3)
                if coint == 1:
                    balance_p = balance + 30
                    cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                    cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(1,id))
                    await call.message.answer(f"Случайный прохожий подарил вам 30 Gamecoin", reply_markup=menu)
                elif coint == 2:
                    balance_p = balance - 15
                    cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                    cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(1,id))
                    await call.message.answer(f"Вы шли по дороге и вас ограбили на 15 Gamecoin", reply_markup=menu)
                else:
                    spisok = ("Пусто", "Пусто", "Пусто", "Пусто","Пусто","Пусто","Пусто","Пузырь","Пусто","Пусто")
                    artefact = random.choice(spisok)
                    if artefact == "Пусто":
                        cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(1,id))
                        await call.message.answer(f"К сожелению артефакт не найден", reply_markup=menu)
                    else:
                        balance_p = balance + 100
                        cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
                        cursors.execute("UPDATE user SET cvest_po=%s WHERE id=%s",(1,id))
                        await call.message.answer(f"Вы нашли артефакт 🫧Пузырь🫧\nАртефакт вам принёс 100 Gamecoin", reply_markup=menu)
            else:
                await call.message.answer(f"Вы уже посещяли квесты приходите завтра", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  артефакт''''''''''''''''''''''''''''''''''''''''''''#'''
async def art(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    names=call.from_user.first_name
    username=call.from_user.username
    await call.message.answer(f"Выберете действия с артифактоми", reply_markup=kbpt)
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  артефакт покупку''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    await call.message.answer(f"Артефакты создана для пасивной прибыли выберите 1 для покупки:", reply_markup=kbpt_art)
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  💍Кольцо подавления💍''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_1(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 10000:
                    await call.message.answer(f"💍Кольцо подавления💍\nОкуп: 34 дня\nЦена: 10000 Gamecoin\nАртефакт приносит:\nПрибыль: 30 Gamecoin", reply_markup=kbpt_art_pok_1)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 10000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  💍Кольцо подавления💍''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p1(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Кольцо подавления"
            balance_p = balance - 10000 # 100 = 5 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 💍Кольцо подавления💍\nС вашего баланса списано 10000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🎎Кукла шамана🎎''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_2(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 15000:
                    await call.message.answer(f"🎎Кукла шамана🎎\nОкуп: 38 - 24 дня\nЦена: 15000 Gamecoin\nАртефакт приносит:\nПрибыль: от 40 до 65 Gamecoin", reply_markup=kbpt_art_pok_2)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 15000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🎎Кукла шамана🎎''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p2(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Кукла шамана"
            balance_p = balance - 15000 # 150 = 8 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 🎎Кукла шамана🎎\nС вашего баланса списано 15000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🧬Кулон разорения🧬''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_3(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 20000:
                    await call.message.answer(f"🧬Кулон разорения🧬\nОкуп: 27 дня\nЦена: 20000 Gamecoin\nАртефакт приносит:\nПрибыль: 75 Gamecoin", reply_markup=kbpt_art_pok_3)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 20000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🧬Кулон разорения🧬''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p3(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Кулон разорения"
            balance_p = balance - 20000 # 200 = 10 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 🧬Кулон разорения🧬\nС вашего баланса списано 20000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🧲Подкова демона🧲''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_4(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 25000:
                    await call.message.answer(f"🧲Подкова демона🧲\nОкуп: 34 - 25 дня\nЦена: 25000 Gamecoin\nАртефакт приносит:\nПрибыль: от 75 до 100 Gamecoin", reply_markup=kbpt_art_pok_4)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 25000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🧲Подкова демона🧲''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p4(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Подкова демона"
            balance_p = balance - 25000 # 250 = 13 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 🧲Подкова демона🧲\nС вашего баланса списано 25000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🦄Рог бездны🦄''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_5(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 30000:
                    await call.message.answer(f"🦄Рог бездны🦄\nОкуп: 24 дня\nЦена: 30000 Gamecoin\nАртефакт приносит:\nПрибыль: 130 Gamecoin", reply_markup=kbpt_art_pok_5)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 30000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🦄Рог бездны🦄''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p5(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Рог бездны"
            balance_p = balance - 30000 # 300 = 15 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 🦄Рог бездны🦄\nС вашего баланса списано 30000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🛡️Щит морской славы🛡️''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_6(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 35000:
                    await call.message.answer(f"🛡️Щит морской славы🛡️\nОкуп: 28 - 24 дня\nЦена: 35000 Gamecoin\nАртефакт приносит:\nПрибыль: от 130 до 150 Gamecoin", reply_markup=kbpt_art_pok_6)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 35000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🛡️Щит морской славы🛡️''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p6(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Щит морской славы"
            balance_p = balance - 35000 # 350 = 18 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 🛡️Щит морской славы🛡️\nС вашего баланса списано 35000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  👢Сапоги странника👢''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_7(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 40000:
                    await call.message.answer(f"👢Сапоги странника👢\nОкуп: 23 дня\nЦена: 40000 Gamecoin\nАртефакт приносит:\nПрибыль: 180 Gamecoin", reply_markup=kbpt_art_pok_7)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 40000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  👢Сапоги странника👢''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p7(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Сапоги странника"
            balance_p = balance - 40000 # 400 = 21 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 👢Сапоги странника👢\nС вашего баланса списано 40000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🔱Трезубец могущества🔱''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_8(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 45000:
                    await call.message.answer(f"🔱Трезубец могущества🔱\nОкуп: 25 - 23 дня\nЦена: 45000 Gamecoin\nАртефакт приносит:\nПрибыль: от 180 до 200 Gamecoin", reply_markup=kbpt_art_pok_8)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 45000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  🔱Трезубец могущества🔱''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p8(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Трезубец могущества"
            balance_p = balance - 45000 # 450 = 23 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 🔱Трезубец могущества🔱\nС вашего баланса списано 45000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  👑Корона пяти морей👑''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_9(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 50000:
                    await call.message.answer(f"👑Корона пяти морей👑\nОкуп: 20 дней\nЦена: 50000 Gamecoin\nАртефакт приносит:\nПрибыль: 250 Gamecoin", reply_markup=kbpt_art_pok_9)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 50000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  👑Корона пяти морей👑''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p9(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Корона пяти морей"
            balance_p = balance - 50000 # 500 = 26 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт 👑Корона пяти морей👑\nС вашего баланса списано 50000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  ⚔️Королевские доспехи⚔️''''''''''''''''''''''''''''''''''''''''''''#'''
async def art_poc_10(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            if artef == "Не куплено":
                if balance >= 76000:
                    await call.message.answer(f"⚔️Королевские доспехи⚔️\nОкуп: 16 дней\nЦена: 76000 Gamecoin\nАртефакт приносит:\nПрибыль: 500 Gamecristall", reply_markup=kbpt_art_pok_10)
                else:
                    await call.message.answer(f"Для покупки этого артефакта вам нужно иметь 76000 Gamecoin,текущий баланс: {balance}", reply_markup=menu)
            else:
                await call.message.answer(f"У тебя уже есть артефакт: {artef},продайте его для покупки нового", reply_markup=menu)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  ⚔️Королевские доспехи⚔️''''''''''''''''''''''''''''''''''''''''''''#'''
async def kbpt_art_pok_p10(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            artef = row['artef']
            artef_p = "Королевские доспехи"
            balance_p = balance - 76000 # 760 = 40 доларов
            cursors.execute("UPDATE user SET artef=%s WHERE id=%s",(artef_p,id))
            cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(balance_p,id))
            await call.message.answer(f"Вы успешно купили артефакт ⚔️Королевские доспехи⚔️\nС вашего баланса списано 76000", reply_markup=menu)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  помощь артефактов''''''''''''''''''''''''''''''''''''''''''''#'''
async def help_art(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    await call.message.answer(f"📖Зачем нужны Артефакты???\n1)Артефакты нужны в первую очередь для вывода Gamecristall\n2)Артефакты нужны для пассивного заработка\n3)Артефакты можно покупать также и продавать\n\n🧾Правила продажи артефактов:\n1)Артефакт вас должен окупить\n2)От стоимости артефакта будет списано рандомный процент от 5% до 10%\n\n📝Можно ли получить артефакт не покупая его?\nДа, можно рандомно в квестах", reply_markup=menu)
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн  дайс''''''''''''''''''''''''''''''''''''''''''''#'''
async def Dic1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Выберете одно число", reply_markup=kbDice)
    
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 1''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDe1_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumD.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎲:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDe1(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumD'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumD']):
                    await message.answer(f"твоя ставка: {data['sumD']} на число 1️⃣",reply_markup=kbDic)
                    await state.finish()
                    numb = data['sumD']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(1,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbDice)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 2''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDe2_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumD2.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎲:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDe2(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumD2'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumD2']):
                    await message.answer(f"твоя ставка: {data['sumD2']} на число 2️⃣",reply_markup=kbDic)
                    await state.finish()
                    numb = data['sumD2']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(2,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbDice)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 3''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDe3_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumD3.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎲:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDe3(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumD3'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumD3']):
                    await message.answer(f"твоя ставка: {data['sumD3']} на число 3️⃣",reply_markup=kbDic)
                    await state.finish()
                    numb = data['sumD3']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(3,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbDice)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 4''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDe4_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumD4.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎲:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDe4(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumD4'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumD4']):
                    await message.answer(f"твоя ставка: {data['sumD4']} на число 4️⃣",reply_markup=kbDic)
                    await state.finish()
                    numb = data['sumD4']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(4,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbDice)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 5''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDe5_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumD5.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎲:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDe5(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumD5'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumD5']):
                    await message.answer(f"твоя ставка: {data['sumD5']} на число 5️⃣",reply_markup=kbDic)
                    await state.finish()
                    numb = data['sumD5']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(5,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbDice)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 6''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDe6_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumD6.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎲:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDe6(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumD6'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumD6']):
                    await message.answer(f"твоя ставка: {data['sumD6']} на число 6️⃣",reply_markup=kbDic)
                    await state.finish()
                    numb = data['sumD6']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(2,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbDice)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Игра дайс''''''''''''''''''''''''''''''''''''''''''''#'''
async def Dice(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            levels = row['levels']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            num = row['num']
            dices = await bot.send_dice(id, emoji="🎲")
            mes = dices.dice.value
            if num == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=rest)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
            else:
                numbalance = balance - levels
                devence = devence + 1
                coln = col + 1
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET devence=%s WHERE id=%s",(devence,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
                connection.commit()
                await call.message.answer(f"Вы проиграли,выпало число: {mes}\nВаш баланс: {balance}", reply_markup=rest)
    connection.commit()


'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн DART''''''''''''''''''''''''''''''''''''''''''''#'''
async def Dart1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Выберете результат игры 🎯", reply_markup=kbdart)
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 1-2''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDa1_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumDA.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎯:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDa1(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumDa'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumDa']):
                    await message.answer(f"твоя ставка: {data['sumDa']} на числа 1️⃣-2️⃣",reply_markup=kbdarts)
                    await state.finish()
                    numb = data['sumDa']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(1,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(2,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbdarts)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 3-4''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDa2_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumDA1.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎯:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDa2(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumDa1'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumDa1']):
                    await message.answer(f"твоя ставка: {data['sumDa1']} на числа 3️⃣-4️⃣",reply_markup=kbdarts)
                    await state.finish()
                    numb = data['sumDa1']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(3,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(4,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbdarts)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 5-6''''''''''''''''''''''''''''''''''''''''''''#'''
async def sumDa3_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumDA2.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎯:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumDa3(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumDa2'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumDa2']):
                    await message.answer(f"твоя ставка: {data['sumDa2']} на числа 5️⃣-6️⃣",reply_markup=kbdarts)
                    await state.finish()
                    numb = data['sumDa2']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(5,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(6,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=kbdarts)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Игра дартс''''''''''''''''''''''''''''''''''''''''''''#'''

async def DARTS(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            levels = row['levels']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            num = row['num']
            num1 = row['num1']
            dart  = await bot.send_dice(id, emoji="🎯")
            mes = dart.dice.value
            if num == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restd)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
            elif num1 == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restd)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(0,id))
            else:
                numbalance = balance - levels
                devence = devence + 1
                coln = col + 1
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET devence=%s WHERE id=%s",(devence,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
                connection.commit()
                await call.message.answer(f"Вы проиграли,выпало число: {mes}\nВаш баланс: {balance}", reply_markup=restd)
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн BASKETBALL''''''''''''''''''''''''''''''''''''''''''''#'''
async def BASKETBALL1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Выберете результат игры 🏀", reply_markup=kbbast)
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 1-2''''''''''''''''''''''''''''''''''''''''''''#'''
async def BASKETBALL1_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumBA.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🏀:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumBASKETBALL1(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumBA'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumBA']):
                    await message.answer(f"твоя ставка: {data['sumBA']} на промах",reply_markup=kbbs)
                    await state.finish()
                    numb = data['sumBA']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(1,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(2,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restbbs)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 3-4''''''''''''''''''''''''''''''''''''''''''''#'''
async def BASKETBALL2_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumBA1.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🏀:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumBASKETBALL2(message: types.Message, state: FSMContext):
    
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumBA1'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumBA1']):
                    await message.answer(f"твоя ставка: {data['sumBA1']} на Застрял",reply_markup=kbbs)
                    await state.finish()
                    numb = data['sumBA1']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(3,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(4,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restbbs)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 5-6''''''''''''''''''''''''''''''''''''''''''''#'''
async def BASKETBALL3_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumBA2.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🏀:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumBASKETBALL3(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumBA2'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumBA2']):
                    await message.answer(f"твоя ставка: {data['sumBA2']} на Попал",reply_markup=kbbs)
                    await state.finish()
                    numb = data['sumBA2']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(5,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(6,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restbbs)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн BASKETBALL''''''''''''''''''''''''''''''''''''''''''''#'''
async def BASKETBALL(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            levels = row['levels']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            num = row['num']
            num1 = row['num1']
            BASKETBALL = await bot.send_dice(id, emoji="🏀")
            mes = BASKETBALL.dice.value
            if num == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restbbs)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
            elif num1 == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restbbs)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(0,id))
            else:
                numbalance = balance - levels
                devence = devence + 1
                coln = col + 1
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET devence=%s WHERE id=%s",(devence,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
                connection.commit()
                await call.message.answer(f"Вы проиграли\nВаш баланс: {balance}", reply_markup=restbbs)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн FOOTBALL''''''''''''''''''''''''''''''''''''''''''''#'''
async def FOOTBALL1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Выберете результат игры ⚽", reply_markup=kbfud)
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 1-2''''''''''''''''''''''''''''''''''''''''''''#'''
async def FOOTBALL_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumFO.set()
                await call.message.answer("Теперь введи вашу ставку на игру ⚽:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumFOOTBALL(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumFO'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumFO']):
                    await message.answer(f"твоя ставка: {data['sumFO']} на Промах",reply_markup=fud)
                    await state.finish()
                    numb = data['sumFO']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(1,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(2,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restfud)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 3-4''''''''''''''''''''''''''''''''''''''''''''#'''
async def FOOTBALL1_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumFO1.set()
                await call.message.answer("Теперь введи вашу ставку на игру ⚽:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumFOOTBALL1(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumFO1'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumFO1']):
                    await message.answer(f"твоя ставка: {data['sumFO1']} на Девятка",reply_markup=fud)
                    await state.finish()
                    numb = data['sumFO1']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(5,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(6,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restfud)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 5-6''''''''''''''''''''''''''''''''''''''''''''#'''
async def FOOTBALL2_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumFO2.set()
                await call.message.answer("Теперь введи вашу ставку на игру ⚽:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumFOOTBALL2(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumFO2'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumFO2']):
                    await message.answer(f"твоя ставка: {data['sumFO2']} на Гол",reply_markup=fud)
                    await state.finish()
                    numb = data['sumFO2']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(3,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(4,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restfud)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн FOOTBALL''''''''''''''''''''''''''''''''''''''''''''#'''
async def FOOTBALL(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            levels = row['levels']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            num = row['num']
            num1 = row['num1']
            FOOTBALL = await bot.send_dice(id, emoji="⚽")
            mes = FOOTBALL.dice.value
            if num == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restfud)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
            elif num1 == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restfud)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(0,id))
            else:
                numbalance = balance - levels
                devence = devence + 1
                coln = col + 1
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET devence=%s WHERE id=%s",(devence,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
                connection.commit()
                await call.message.answer(f"Вы проиграли\nВаш баланс: {balance}", reply_markup=restfud)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн SLOT_MACHINE''''''''''''''''''''''''''''''''''''''''''''#'''
async def SLOT_MACHINE1(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumSL.set()
                await call.message.answer(f"Введите ставка на игру 🎰, твой баланс: {balance}")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumSLOT_MACHINE(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumSL'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumSL']):
                    await message.answer(f"твоя ставка: {data['sumSL']}",reply_markup=kbslot)
                    await state.finish()
                    numb = data['sumSL']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restslot)
    connection.commit()


'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн SLOT_MACHINE''''''''''''''''''''''''''''''''''''''''''''#'''
async def SLOT_MACHINE(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            levels = row['levels']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            SLOT_MACHINE = await bot.send_dice(id, emoji="🎰")
            mes = SLOT_MACHINE.dice.value
            if int(mes) == 43:
                balanceV = levels*2.5
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю выпали лимоны,ваш Gamecoin баланс: {numbalance}", reply_markup=restslot)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
            elif int(mes) == 1:
                balanceV = levels*2
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю выпал бар,ваш Gamecoin баланс: {numbalance}", reply_markup=restslot)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
            elif int(mes) == 22:
                balanceV = levels*1.5
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю выпал виноград,ваш Gamecoin баланс: {numbalance}", reply_markup=restslot)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
            elif int(mes) == 64:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю выпали семёрки,ваш Gamecoin баланс: {numbalance}", reply_markup=restslot)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
            else:
                numbalance = balance - levels
                devence = devence + 1
                coln = col + 1
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET devence=%s WHERE id=%s",(devence,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                connection.commit()
                await call.message.answer(f"Вы проиграли\nВаш баланс: {balance}", reply_markup=restslot)
    connection.commit()
                
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн BOWLING''''''''''''''''''''''''''''''''''''''''''''#'''
async def BOWLING1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Выберете результат игры 🎳", reply_markup=kbbow)
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 1-2''''''''''''''''''''''''''''''''''''''''''''#'''
async def BOWLING_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumBO.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎳:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumBOWLING(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumBO'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumBO']):
                    await message.answer(f"твоя ставка: {data['sumBO']} на Промах",reply_markup=kbbowl)
                    await state.finish()
                    numb = data['sumBO']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(1,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(2,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restfud)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 3-4''''''''''''''''''''''''''''''''''''''''''''#'''
async def BOWLING1_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumBO1.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎳:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumBOWLING1(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumBO1'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumBO1']):
                    await message.answer(f"твоя ставка: {data['sumBO1']} на Есть остаток",reply_markup=kbbowl)
                    await state.finish()
                    numb = data['sumBO1']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(3,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(4,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restfud)
    connection.commit()
    
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры 5-6''''''''''''''''''''''''''''''''''''''''''''#'''
async def BOWLING2_text(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            if balance >= 10:
                await FSMclient.sumBO2.set()
                await call.message.answer("Теперь введи вашу ставку на игру 🎳:")
            else:
                await call.message.answer("недостаточно Gamecoin для игры\nТвой баланс: {balance}",reply_markup=menu)

async def sumBOWLING2(message: types.Message, state: FSMContext):
    id = message.from_user.id
    async with state.proxy() as data:
        data['sumBO2'] = message.text
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            async with state.proxy() as data:
                if int(balance) >= int(data['sumBO2']):
                    await message.answer(f"твоя ставка: {data['sumBO2']} на Страйк",reply_markup=kbbowl)
                    await state.finish()
                    numb = data['sumBO2']
                    cursors.execute("UPDATE user SET levels=%s WHERE id=%s",(numb,id))
                    cursors.execute("UPDATE user SET num=%s WHERE id=%s",(5,id))
                    cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(6,id))
                else:
                    await message.answer(f"недостаточно Gamecoin для текущей ставки\nТекущий баланс: {balance}",reply_markup=restfud)
    connection.commit()
'''#''''''''''''''''''''''''''''''''''''''''обработчик инлайн BOWLING''''''''''''''''''''''''''''''''''''''''''''#'''
async def BOWLING(call: CallbackQuery):
    await call.message.delete()
    id = call.from_user.id
    with connection.cursor() as cursors:
        cursors.execute(f"SELECT * FROM user WHERE id={id}")
        for row in cursors:
            balance = row['balance']
            levels = row['levels']
            victory = row['victory']
            devence = row['devence']
            col = row['col']
            num = row['num']
            num1 = row['num1']
            BOWLING = await bot.send_dice(id, emoji="🎳")
            mes= BOWLING.dice.value
            if num == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restbow)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
            elif num1 == mes:
                balanceV = levels*3
                numbalance = balance + balanceV
                victoryn = victory + 1
                coln = col + 1
                await call.message.answer(f"Поздравяляю вы выиграли Gamecoin\n Gamecoin баланс: {numbalance}", reply_markup=restbow)
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET victory=%s WHERE id=%s",(victoryn,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num1=%s WHERE id=%s",(0,id))
            else:
                numbalance = balance - levels
                devence = devence + 1
                coln = col + 1
                cursors.execute("UPDATE user SET balance=%s WHERE id=%s",(numbalance,id))
                cursors.execute("UPDATE user SET devence=%s WHERE id=%s",(devence,id))
                cursors.execute("UPDATE user SET col=%s WHERE id=%s",(coln,id))
                cursors.execute("UPDATE user SET num=%s WHERE id=%s",(0,id))
                connection.commit()
                await call.message.answer(f"Вы проиграли\nВаш баланс: {balance}", reply_markup=restbow)
    connection.commit()


async def prize_btn(call: CallbackQuery):
    await call.message.delete()
    balance = 0
    balance_ran = random.randint(50,1000)
    balance += balance_ran
    await call.message.answer(f"Приз: {balance_ran}\nБаланс: {balance}", reply_markup=kb1)
    

'''#''''''''''''''''''''''''''''''''''''''''регистр''''''''''''''''''''''''''''''''''''''''''''#'''
def register_handlers_client(dp: Dispatcher):
    dp.register_callback_query_handler(Prof, text="Prof")
    dp.register_callback_query_handler(obmen, text="obmen", state=None)
    dp.register_message_handler(obmen_game, state=FSMclient.obm)
    dp.register_callback_query_handler(Menu, text="Menu")
    dp.register_message_handler(greetings, content_types=['new_chat_members'])
    dp.register_message_handler(start_bot, commands=['start'])
    dp.register_callback_query_handler(DARTS, text="DARTS")
    dp.register_callback_query_handler(Dart1, text="Dart1")
    dp.register_callback_query_handler(sumDa1_text, text="sumDa1_text", state=None)
    dp.register_message_handler(sumDa1, state=FSMclient.sumDA)
    dp.register_callback_query_handler(sumDa2_text, text="sumDa2_text", state=None)
    dp.register_message_handler(sumDa2, state=FSMclient.sumDA1)
    dp.register_callback_query_handler(sumDa3_text, text="sumDa3_text", state=None)
    dp.register_message_handler(sumDa3, state=FSMclient.sumDA2)
    dp.register_callback_query_handler(Game, text="Game")
    dp.register_callback_query_handler(BASKETBALL, text="BASKETBALL")
    dp.register_callback_query_handler(BASKETBALL1, text="BASKETBALL1")
    dp.register_callback_query_handler(BASKETBALL1_text, text="BASKETBALL1_text", state=None)
    dp.register_message_handler(sumBASKETBALL1, state=FSMclient.sumBA)
    dp.register_callback_query_handler(BASKETBALL2_text, text="BASKETBALL2_text", state=None)
    dp.register_message_handler(sumBASKETBALL2, state=FSMclient.sumBA1)
    dp.register_callback_query_handler(BASKETBALL3_text, text="BASKETBALL3_text", state=None)
    dp.register_message_handler(sumBASKETBALL3, state=FSMclient.sumBA2)
    dp.register_callback_query_handler(Dic1, text="Dic1")
    dp.register_callback_query_handler(Dice, text="Dice")
    dp.register_callback_query_handler(sumDe1_text, text="sumDe1_text", state=None)
    dp.register_message_handler(sumDe1, state=FSMclient.sumD)
    dp.register_callback_query_handler(sumDe2_text, text="sumDe2_text", state=None)
    dp.register_message_handler(sumDe2, state=FSMclient.sumD2)
    dp.register_callback_query_handler(sumDe3_text, text="sumDe3_text", state=None)
    dp.register_message_handler(sumDe3, state=FSMclient.sumD3)
    dp.register_callback_query_handler(sumDe4_text, text="sumDe4_text", state=None)
    dp.register_message_handler(sumDe4, state=FSMclient.sumD4)
    dp.register_callback_query_handler(sumDe5_text, text="sumDe5_text", state=None)
    dp.register_message_handler(sumDe5, state=FSMclient.sumD5)
    dp.register_callback_query_handler(sumDe6_text, text="sumDe6_text", state=None)
    dp.register_message_handler(sumDe6, state=FSMclient.sumD6)
    dp.register_callback_query_handler(FOOTBALL, text="FOOTBALL")
    dp.register_callback_query_handler(FOOTBALL1, text="FOOTBALL1")
    dp.register_callback_query_handler(FOOTBALL_text, text="FOOTBALL_text", state=None)
    dp.register_message_handler(sumFOOTBALL, state=FSMclient.sumFO)
    dp.register_callback_query_handler(FOOTBALL1_text, text="FOOTBALL1_text", state=None)
    dp.register_message_handler(sumFOOTBALL1, state=FSMclient.sumFO1)
    dp.register_callback_query_handler(FOOTBALL2_text, text="FOOTBALL2_text", state=None)
    dp.register_message_handler(sumFOOTBALL2, state=FSMclient.sumFO2)
    dp.register_callback_query_handler(SLOT_MACHINE, text="SLOT_MACHINE")
    dp.register_callback_query_handler(SLOT_MACHINE1, text="SLOT_MACHINE1", state=None)
    dp.register_message_handler(sumSLOT_MACHINE, state=FSMclient.sumSL)
    dp.register_callback_query_handler(BOWLING, text="BOWLING")
    dp.register_callback_query_handler(BOWLING1, text="BOWLING1")
    dp.register_callback_query_handler(BOWLING_text, text="BOWLING_text", state=None)
    dp.register_message_handler(sumBOWLING, state=FSMclient.sumBO)
    dp.register_callback_query_handler(BOWLING1_text, text="BOWLING1_text", state=None)
    dp.register_message_handler(sumBOWLING1, state=FSMclient.sumBO1)
    dp.register_callback_query_handler(BOWLING2_text, text="BOWLING2_text", state=None)
    dp.register_message_handler(sumBOWLING2, state=FSMclient.sumBO2)
    dp.register_callback_query_handler(art, text="art")
    dp.register_callback_query_handler(art_poc, text="art_poc")
    dp.register_callback_query_handler(art_poc_1, text="art_poc_1")
    dp.register_callback_query_handler(kbpt_art_pok_p1, text="kbpt_art_pok_p1")
    dp.register_callback_query_handler(art_poc_2, text="art_poc_2")
    dp.register_callback_query_handler(kbpt_art_pok_p2, text="kbpt_art_pok_p2")
    dp.register_callback_query_handler(art_poc_3, text="art_poc_3")
    dp.register_callback_query_handler(kbpt_art_pok_p3, text="kbpt_art_pok_p3")
    dp.register_callback_query_handler(art_poc_4, text="art_poc_4")
    dp.register_callback_query_handler(kbpt_art_pok_p4, text="kbpt_art_pok_p4")
    dp.register_callback_query_handler(art_poc_5, text="art_poc_5")
    dp.register_callback_query_handler(kbpt_art_pok_p5, text="kbpt_art_pok_p5")
    dp.register_callback_query_handler(art_poc_6, text="art_poc_6")
    dp.register_callback_query_handler(kbpt_art_pok_p6, text="kbpt_art_pok_p6")
    dp.register_callback_query_handler(art_poc_7, text="art_poc_7")
    dp.register_callback_query_handler(kbpt_art_pok_p7, text="kbpt_art_pok_p7")
    dp.register_callback_query_handler(art_poc_8, text="art_poc_8")
    dp.register_callback_query_handler(kbpt_art_pok_p8, text="kbpt_art_pok_p8")
    dp.register_callback_query_handler(art_poc_9, text="art_poc_9")
    dp.register_callback_query_handler(kbpt_art_pok_p9, text="kbpt_art_pok_p9")
    dp.register_callback_query_handler(art_poc_10, text="art_poc_10")
    dp.register_callback_query_handler(kbpt_art_pok_p10, text="kbpt_art_pok_p10")
    dp.register_callback_query_handler(help_art, text="help_art")
    dp.register_callback_query_handler(cvest, text="cvest")
    dp.register_callback_query_handler(Info, text="Info")
    dp.register_callback_query_handler(prize_btn, text="Подарок")
    dp.register_callback_query_handler(pop, text="pop")
    dp.register_callback_query_handler(viv, text="viv")


