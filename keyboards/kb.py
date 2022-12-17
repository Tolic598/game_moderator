from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

'''#''''''''''''''''''''''''''''''''''''''''Запус меню''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="💠Профиль💠", callback_data="Prof")
b2  = InlineKeyboardButton(text="📜Квест📜", callback_data="cvest")
b3  = InlineKeyboardButton(text="🔮Артефакты🔮", callback_data="art")
b4  = InlineKeyboardButton(text="🎮Игры🎮", callback_data="Game")
b5  = InlineKeyboardButton(text="🗣️Информация📃", callback_data="Info")
menu = InlineKeyboardMarkup(row_width=1)
menu.row(b1).row(b2,b3).row(b4).row(b5)

'''#''''''''''''''''''''''''''''''''''''''''Запуск игры''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🎯", callback_data="Dart1")
b2  = InlineKeyboardButton(text="🏀", callback_data="BASKETBALL1")
b3  = InlineKeyboardButton(text="🎲", callback_data="Dic1")
b4  = InlineKeyboardButton(text="⚽", callback_data="FOOTBALL1")
b5  = InlineKeyboardButton(text="🎰", callback_data="SLOT_MACHINE")
b6  = InlineKeyboardButton(text="🎳", callback_data="BOWLING1")
b7  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kb = InlineKeyboardMarkup(row_width=1)
kb.row(b1,b2,b3).row(b4,b5,b6).row(b7) #в ряд

'''#''''''''''''''''''''''''''''''''''''''''игра дайс''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🪬Играть🪬", callback_data="Dice")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbDic = InlineKeyboardMarkup(row_width=1)
kbDic.row(b1).row(b2)

'''#''''''''''''''''''''''''''''''''''''''''игра дартс''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🪬Играть🪬", callback_data="DARTS")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbdarts = InlineKeyboardMarkup(row_width=1)
kbdarts.row(b1).row(b2)
'''#''''''''''''''''''''''''''''''''''''''''игра баскетбол''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🪬Играть🪬", callback_data="BASKETBALL")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbbs = InlineKeyboardMarkup(row_width=1)
kbbs.row(b1).row(b2)
'''#''''''''''''''''''''''''''''''''''''''''игра футбол''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🪬Играть🪬", callback_data="FOOTBALL")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
fud = InlineKeyboardMarkup(row_width=1)
fud.row(b1).row(b2)
'''#''''''''''''''''''''''''''''''''''''''''игра слот''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🪬Крутить🪬", callback_data="SLOT_MACHINE")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbslot = InlineKeyboardMarkup(row_width=1)
kbslot.row(b1).row(b2)

'''#''''''''''''''''''''''''''''''''''''''''игра боулинг''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🪬Играть🪬", callback_data="BOWLING")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbbowl = InlineKeyboardMarkup(row_width=1)
kbbowl.row(b1).row(b2)

'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры на баскетбол''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="Попал", callback_data="BASKETBALL3_text")
b2  = InlineKeyboardButton(text="Застрял", callback_data="BASKETBALL2_text")
b3  = InlineKeyboardButton(text="Промах", callback_data="BASKETBALL1_text")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbbast = InlineKeyboardMarkup(row_width=1)
kbbast.row(b1,b2,b3).row(b4) #в ряд

'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры на футбол''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="Гол", callback_data="FOOTBALL2_text")
b2  = InlineKeyboardButton(text="Девятка", callback_data="FOOTBALL1_text")
b3  = InlineKeyboardButton(text="Промах", callback_data="FOOTBALL_text")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbfud = InlineKeyboardMarkup(row_width=1)
kbfud.row(b1,b2,b3).row(b4) #в ряд
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры на дайс''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="1️⃣-2️⃣", callback_data="sumDa1_text")
b2  = InlineKeyboardButton(text="3️⃣-4️⃣", callback_data="sumDa2_text")
b3  = InlineKeyboardButton(text="5️⃣-6️⃣", callback_data="sumDa3_text")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbdart = InlineKeyboardMarkup(row_width=1)
kbdart.row(b1,b2,b3).row(b4) #в ряд
'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="1️⃣", callback_data="sumDe1_text")
b2  = InlineKeyboardButton(text="2️⃣", callback_data="sumDe2_text")
b3  = InlineKeyboardButton(text="3️⃣", callback_data="sumDe3_text")
b4  = InlineKeyboardButton(text="4️⃣", callback_data="sumDe4_text")
b5  = InlineKeyboardButton(text="5️⃣", callback_data="sumDe5_text")
b6  = InlineKeyboardButton(text="6️⃣", callback_data="sumDe6_text")
b7  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbDice = InlineKeyboardMarkup(row_width=1)
kbDice.row(b1,b2,b3).row(b4,b5,b6).row(b7) #в ряд

'''#''''''''''''''''''''''''''''''''''''''''Выбор цыфры на боулинг''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="Страйк", callback_data="BOWLING2_text")
b2  = InlineKeyboardButton(text="Есть остаток", callback_data="BOWLING1_text")
b3  = InlineKeyboardButton(text="Промах", callback_data="BOWLING_text")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbbow = InlineKeyboardMarkup(row_width=1)
kbbow.row(b1,b2,b3).row(b4) #в ряд

'''#''''''''''''''''''''''''''''''''''''''''Ввод суммы''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="ввести сумму", callback_data="sumD")
b2  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbsum = InlineKeyboardMarkup(row_width=1)
kbsum.row(b1).row(b2)

'''#''''''''''''''''''''''''''''''''''''''''Запус крута''''''''''''''''''''''''''''''''''''''''''''#'''
b2  = InlineKeyboardButton(text="🎁", callback_data="Подарок")
kb1 = InlineKeyboardMarkup(row_width=1)
kb1.row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2).row(b2, b2, b2, b2, b2)
'''#''''''''''''''''''''''''''''''''''''''''Подробней о бонусах''''''''''''''''''''''''''''''''''''''''''''#'''
kb2 = InlineKeyboardMarkup()
button = InlineKeyboardButton('📖 Подробнее о бонусах', url='https://google.com')
kb2.add(button)


'''#''''''''''''''''''''''''''''''''''''''''Запус рестарта''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Играть ещё раз🔄", callback_data="Dic1")
b2  = InlineKeyboardButton(text="🕹️Выбрать другую игру🕹️", callback_data="Game")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
rest = InlineKeyboardMarkup(row_width=1)
rest.row(b1).row(b2).row(b3)
'''#''''''''''''''''''''''''''''''''''''''''Запус рестарта дайс''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Играть ещё раз🔄", callback_data="Dart1")
b2  = InlineKeyboardButton(text="🕹️Выбрать другую игру🕹️", callback_data="Game")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
restd = InlineKeyboardMarkup(row_width=1)
restd.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''Запус рестарта баскетбол''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Играть ещё раз🔄", callback_data="BASKETBALL1")
b2  = InlineKeyboardButton(text="🕹️Выбрать другую игру🕹️", callback_data="Game")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
restbbs = InlineKeyboardMarkup(row_width=1)
restbbs.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''Запус рестарта футбол''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Играть ещё раз🔄", callback_data="FOOTBALL")
b2  = InlineKeyboardButton(text="💰Выбрать другую ставку💰", callback_data="FOOTBALL1")
b3  = InlineKeyboardButton(text="🕹️Выбрать другую игру🕹️", callback_data="Game")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
restfud = InlineKeyboardMarkup(row_width=1)
restfud.row(b1).row(b2).row(b3).row(b4)
'''#''''''''''''''''''''''''''''''''''''''''Запус рестарта слот''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Играть ещё раз🔄", callback_data="SLOT_MACHINE")
b2  = InlineKeyboardButton(text="💰Выбрать другую ставку💰", callback_data="SLOT_MACHINE1")
b3  = InlineKeyboardButton(text="🕹️Выбрать другую игру🕹️", callback_data="Game")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
restslot = InlineKeyboardMarkup(row_width=1)
restslot.row(b1).row(b2).row(b3)
'''#''''''''''''''''''''''''''''''''''''''''Запус рестарта боулинг''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Играть ещё раз🔄", callback_data="BOWLING")
b2  = InlineKeyboardButton(text="💰Выбрать другую ставку💰", callback_data="BOWLING1")
b3  = InlineKeyboardButton(text="🕹️Выбрать другую игру🕹️", callback_data="Game")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
restbow = InlineKeyboardMarkup(row_width=1)
restbow.row(b1).row(b2).row(b3).row(b4)
'''#''''''''''''''''''''''''''''''''''''''''Запус меню профиля''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔄Обменик🔄", callback_data="obmen")
b2  = InlineKeyboardButton(text="📥Пополнить📥", callback_data="pop")
b3  = InlineKeyboardButton(text="📤Вывести📤", callback_data="viv")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
menuprof = InlineKeyboardMarkup(row_width=1)
menuprof.row(b1).row(b2,b3).row(b4)

'''#''''''''''''''''''''''''''''''''''''''''артефакты''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🔮Покупка артефактов🔮", callback_data="art_poc")
b2  = InlineKeyboardButton(text="🛢️Продажа артефактов🛢️", callback_data="art_prod")
b3  = InlineKeyboardButton(text="📃Помощь📃", callback_data="help_art")
b4  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt = InlineKeyboardMarkup(row_width=1)
kbpt.row(b1).row(b2).row(b3).row(b4) #в ряд

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="💍Кольцо подавления💍", callback_data="art_poc_1")
b2  = InlineKeyboardButton(text="🎎Кукла шамана🎎", callback_data="art_poc_2")
b3  = InlineKeyboardButton(text="🧬Кулон разорения🧬", callback_data="art_poc_3")
b4  = InlineKeyboardButton(text="🧲Подкова демона🧲", callback_data="art_poc_4")
b5  = InlineKeyboardButton(text="🦄Рог бездны🦄", callback_data="art_poc_5")
b6  = InlineKeyboardButton(text="🛡️Щит морской славы🛡️", callback_data="art_poc_6")
b7= InlineKeyboardButton(text="👢Сапоги странника👢", callback_data="art_poc_7")
b8  = InlineKeyboardButton(text="🔱Трезубец могущества🔱", callback_data="art_poc_8")
b9  = InlineKeyboardButton(text="👑Корона пяти морей👑", callback_data="art_poc_9")
b10 = InlineKeyboardButton(text="⚔️Королевские доспехи⚔️", callback_data="art_poc_10")
b11  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art = InlineKeyboardMarkup(row_width=1)
kbpt_art.row(b1,b2,b3).row(b4,b5,b6).row(b7,b8 ,b9).row(b10).row(b11)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 💍Кольцо подавления💍''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p1")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_1 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_1.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 🎎Кукла шамана🎎''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p2")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_2 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_2.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 🧬Кулон разорения🧬''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p3")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_3 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_3.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 🧲Подкова демона🧲''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p4")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_4 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_4.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 🦄Рог бездны🦄''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p5")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_5 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_5.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 🛡️Щит морской славы🛡️''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p6")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_6 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_6.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 👢Сапоги странника👢''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p7")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_7 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_7.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 🔱Трезубец могущества🔱''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p8")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_8 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_8.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка 👑Корона пяти морей👑''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p9")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_9 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_9.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''артефакты покупка ⚔️Королевские доспехи⚔️''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="🏪Купить🏪", callback_data="kbpt_art_pok_p10")
b2  = InlineKeyboardButton(text="🔙Отмена🔙", callback_data="art")
b3  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbpt_art_pok_10 = InlineKeyboardMarkup(row_width=1)
kbpt_art_pok_10.row(b1).row(b2).row(b3)

'''#''''''''''''''''''''''''''''''''''''''''Админка для админов''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="Текущие приветствие", callback_data="greetings_chat_t")
b2  = InlineKeyboardButton(text="Приветствие в чат", callback_data="greetings_chat")
b3  = InlineKeyboardButton(text="Приветствие в чат + картинка", callback_data="greetings_chat_photo")
kbadmin_chat = InlineKeyboardMarkup(row_width=1)
kbadmin_chat.row(b1).row(b2,b3)

'''#''''''''''''''''''''''''''''''''''''''''Админка''''''''''''''''''''''''''''''''''''''''''''#'''
b1  = InlineKeyboardButton(text="📝Рассылка текста в бот📝", callback_data="ras_chat")
b2  = InlineKeyboardButton(text="✉️Рассылка текста в бот + картинки✉️", callback_data="ras_chat_photo")
b3  = InlineKeyboardButton(text="🗞️Рассылка текста в чат🗞️", callback_data="ras_chat_ls")
b4  = InlineKeyboardButton(text="📨Рассылка текста в чат + картинки📨", callback_data="ras_chat_photo_ls")
b5  = InlineKeyboardButton(text="🏠Главное меню🏠", callback_data="Menu")
kbadmin = InlineKeyboardMarkup(row_width=1)
kbadmin.row(b1,b2).row(b3,b4).row(b5) #в ряд
