# -*- coding: utf8 -*-
################################################################################################################################
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
#################################################################################################################################
 
######################################################################
from aiogram.dispatcher import FSMContext ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
from aiogram.dispatcher.filters import Command ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
from aiogram.contrib.fsm_storage.memory import MemoryStorage ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
from aiogram.dispatcher.filters.state import StatesGroup, State ## ТО, ЧЕГО ВЫ ЖДАЛИ - FSM
######################################################################
 
######################
import config ## ИМПОРТИРУЕМ ДАННЫЕ ИЗ ФАЙЛОВ config.py
import keyboard ## ИМПОРТИРУЕМ ДАННЫЕ ИЗ ФАЙЛОВ keyboard.py
######################
 
import logging # ПРОСТО ВЫВОДИТ В КОНСОЛЬ ИНФОРМАЦИЮ, КОГДА БОТ ЗАПУСТИТСЯ
import random
import asyncio
import datetime
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from aiogram.utils.deep_linking import get_start_link, decode_payload
from aiogram import types









storage = MemoryStorage() # FOR FSM
bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
 
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s] %(message)s',
 level=logging.INFO,
 )


class meinfo(StatesGroup):
    Q1 = State()
    Q2 = State()


@dp.message_handler(Command("me"), state=None)        # Создаем команду /me для админа.
async def enter_meinfo(message: types.Message):
    if message.chat.id == config.admin:               
        await message.answer("начинаем настройку.\n"        # Бот спрашивает ссылку
                         "№1 Введите линк на вашу новость, Король.")

        await meinfo.Q1.set()                                    # и начинает ждать наш ответ.

@dp.message_handler(state=meinfo.Q1)                                # Как только бот получит ответ, вот это выполнится
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)                            # тут же он записывает наш ответ (наш линк)

    await message.answer("Линк сохранён. \n"
                         "№2 Введите текст для описания новости.")
    await meinfo.Q2.set()                                    # дальше ждёт пока мы введем текст


@dp.message_handler(state=meinfo.Q2)                    # Текст пришел а значит переходим к этому шагу
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text 
    await state.update_data(answer2=answer)                # опять же он записывает второй ответ

    await message.answer("Текст сохранён.")

    data = await state.get_data()                #
    answer1 = data.get("answer1")                # тут он сует ответы в переменную, чтобы сохранить их в "БД" и вывести в след. сообщении
    answer2 = data.get("answer2")                #

    joinedFile = open("link.txt","w", encoding="utf-8")        # Вносим в "БД" encoding="utf-8" НУЖЕН ДЛЯ ТОГО, ЧТОБЫ ЗАПИСЫВАЛИСЬ СМАЙЛИКИ
    joinedFile.write(str(answer1))
    joinedFile = open("text.txt","w", encoding="utf-8")        # Вносим в "БД" encoding="utf-8" НУЖЕН ДЛЯ ТОГО, ЧТОБЫ ЗАПИСЫВАЛИСЬ СМАЙЛИКИ
    joinedFile.write(str(answer2))

    await message.answer(f'Ваша ссылка на профиль: {answer1}\nВаш текст:\n{answer2}')    # Ну и выводим линк с текстом который бот записал
 
    await state.finish()











###############################################################################КОМАНДЫ ЧЕРЕЗ /#############################################################################

@dp.message_handler(Command("other"), state=None)

async def other(message):
    await bot.send_message(message.chat.id, f"*🥺*",  reply_markup=keyboard.other, parse_mode='Markdown')


@dp.message_handler(Command("keys"), state=None)

async def keys(message):
    await bot.send_message(message.chat.id, f"*Клавиатура открыта ⌨️ \n\nДля справки жми: /bothelp 📖*",  reply_markup=keyboard.keys, parse_mode='Markdown')


@dp.message_handler(Command("ref"), state=None)

async def ref(message):
    await bot.send_message(message.chat.id, f"*За КАЖДОГО приглашенного друга приятная скидка на услуги:)*", reply_markup=keyboard.ref, parse_mode='Markdown')
    args = message.get_args()
    reference = decode_payload(args)
    await message.answer(f"*Ваш реферал: {reference}\n\nподробнее: /ref*", reply_markup=keyboard.ref, parse_mode='Markdown') #здесь в  reference должен быть юзернейм, того кто создал ссылку

    

@dp.message_handler(Command("pack"), state=None)

async def pack(message):
    await bot.send_message(message.chat.id, f"*Наша статистика за последние 2 месяца 📊 \n\nДля выхода используй команду: /menu*",  reply_markup=keyboard.pack, parse_mode='Markdown')


@dp.message_handler(Command("manager"), state=None)

async def manager(message):
    await bot.send_message(message.chat.id, f"*Для связи с менеджером жми кнопку🤖 \n\nДля выхода используй команду: /menu*",  reply_markup=keyboard.manager, parse_mode='Markdown')


@dp.message_handler(Command("done"), state=None)

async def done(message):
    await bot.send_message(message.chat.id, f"*Наша статистика за последние 2 месяца📊 \n\nДля выхода используй команду: /menu*",  reply_markup=keyboard.done, parse_mode='Markdown')



@dp.message_handler(Command("pay"), state=None)

async def pay(message):
    await bot.send_message(message.chat.id, f"*Для оплаты выбери удобный способ:💵 \n\nДля выхода используй команду: /menu*",  reply_markup=keyboard.pay, parse_mode='Markdown')





@dp.message_handler(Command("menu"), state=None)

async def menu(message):
    await bot.send_message(message.chat.id, f"*Если заблудился:) \n\nВсегда есть команда: /bothelp 📖*",  reply_markup=keyboard.menu, parse_mode='Markdown')


@dp.message_handler(Command("connect"), state=None)

async def connect(message):
    await bot.send_message(message.chat.id, f"*Нажми <Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲> \n\nДля выхода команда: /menu 📴*",  reply_markup=keyboard.connect, parse_mode='Markdown')



@dp.message_handler(Command("bothelp"), state=None)
async def bothelp(message):
    await bot.send_message(message.chat.id, f"*❗️ Привет, я — бот Авитолог, созданный для  твоего продвижения на авито:) \n\nЯ предлагаю тебе выгодные условия для продвижения, показываю результаты заказов и статистику нашей команды, предлагаю пакеты услуг📋. \n\nВсе просто: \n ___Приводи друзей в бота и получай скидку за КАЖДОГО друга в (/ref)💵\n___Выбирай услугу, в <Пᴩᴀйᴄ-ᴧиᴄᴛ📃> (/pack), запоминай номер \n ___Далее нажимай кнопку: <Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈> (/manager ) \n___Говори номер услуги, или просто спроси про свою нишу и условия \n___Так же можешь оплатить услугу тут в <Ꮻᴨᴧᴀᴛᴀ💸>(/pay), ❗️главное  укажи в комментариях ссылку на профиль и услугу ❗️ \n___Смотри наши выполненные заказы (/done) ✅ \n___Наши клиенты имеют постоянные скидки на следующие заказы, нас выбирают именно за качество выполнения заказов, а так же наша команда самая ответственная и дружелюбна на рынке, присоединяйся❗️ \n\n\nОсновные команды: \n/start - Перезапустить бота🔁 \n/ref - Реферальная система🕺\n/keys - Вводи в любой непонятной ситуации🗿 \n/bothelp - Откроет это окно🧾 \n/menu - Открывает нижнее меню💻 \n/connect - Общение между клиентами👩‍💻 \n/manager - Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈 \n/pack - Пᴩᴀйᴄ-ᴧиᴄᴛ📃 \n/pay - Ꮻᴨᴧᴀᴛᴀ💸\n/done - Выполненные заказы✅*", reply_markup=keyboard.start, parse_mode='Markdown')
   


@dp.message_handler(Command("admin"), state=None)
async def admin(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Привет🥺 \nАдмин {message.from_user.first_name}*",  reply_markup=keyboard.admin, parse_mode='Markdown')
        joinedFile = open("user.txt","r")
        joinedUsers = set ()
        for line in joinedFile:
            jionedUsers.add(line.strip())
        joinedFile.close()
    else:
        await bot.send_message(message.chat.id, f"*У тебя нет админки, увы...😪*", parse_mode='Markdown')



@dp.message_handler(Command("start"), state=None)

async def welcome(message):
    joinedFile = open("user.txt","r")
    joinedUsers = set ()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt","a")
        joinedFile.write(str(message.chat.id)+ "\n")
        joinedUsers.add(message.chat.id)


    await bot.send_message(message.chat.id, f"*❗️ Привет, я — бот Авитолог, созданный для  твоего продвижения на авито:) \n\nЯ предлагаю тебе выгодные условия для продвижения, показываю результаты заказов и статистику нашей команды, предлагаю пакеты услуг📋. \n\nВсе просто: \n ___Приводи друзей в бота и получай скидку за КАЖДОГО друга в (/ref)💵💵\n___Выбирай услугу, в <Пᴩᴀйᴄ-ᴧиᴄᴛ📃> (/pack), запоминай номер \n ___Далее нажимай кнопку: <Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈> (/manager ) \n___Говори номер услуги, или просто спроси про свою нишу и условия \n___Так же можешь оплатить услугу тут в <Ꮻᴨᴧᴀᴛᴀ💸>(/pay), ❗️главное  укажи в комментариях ссылку на профиль и услугу ❗️ \n___Смотри наши выполненные заказы (/done) ✅ \n___Наши клиенты имеют постоянные скидки на следующие заказы, нас выбирают именно за качество выполнения заказов, а так же наша команда самая ответственная и дружелюбна на рынке, присоединяйся❗️ \n\n\nОсновные команды: \n/start - Перезапустить бота🔁 \n/ref - Реферальная система🕺\n/keys - Вводи в любой непонятной ситуации🗿 \n/bothelp - Откроет это окно🧾 \n/menu - Открывает нижнее меню💻 \n/connect - Общение между клиентами👩‍💻 \n/manager - Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈 \n/pack - Пᴩᴀйᴄ-ᴧиᴄᴛ📃 \n/pay - Ꮻᴨᴧᴀᴛᴀ💸\n/done - Выполненные заказы✅*", reply_markup=keyboard.start, parse_mode='Markdown')
   


@dp.message_handler(commands=['rassilka'])
async def rassilka(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась \nБот оповестит когда рассылку закончит*", parse_mode='Markdown')
        receive_users, block_users = 0, 0
        joinedFile = open ("user.txt", "r")
        jionedUsers = set ()
        for line in joinedFile:
            jionedUsers.add(line.strip())
        joinedFile.close()
        for user in jionedUsers:
            try:
                await bot.send_photo(user, open('lzt.png', 'rb'), message.text[message.text.find(' '):])
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await bot.send_message(message.chat.id, f"*Рассылка была завершена *\n"
                                                              f"получили сообщение: *{receive_users}*\n"
                                                              f"заблокировали бота: *{block_users}*", parse_mode='Markdown')







        

@dp.message_handler(commands=['rassilka'])
async def rassilka(message):
    if message.chat.id == config.admin:
        await bot.send_message(message.chat.id, f"*Рассылка началась \nБот оповестит когда рассылку закончит*", parse_mode='Markdown')
        receive_users, block_users = 0, 0
        joinedFile = open ("user.txt", "r")
        jionedUsers = set ()
        for line in joinedFile:
            jionedUsers.add(line.strip())
        joinedFile.close()
        for user in jionedUsers:
            try:
                await bot.send_photo(user, open('lzt.png', 'rb'), message.text[message.text.find(' '):])
                receive_users += 1
            except:
                block_users += 1
            await asyncio.sleep(0.4)
        await bot.send_message(message.chat.id, f"*Рассылка была завершена *\n"
                                                              f"получили сообщение: *{receive_users}*\n"
                                                              f"заблокировали бота: *{block_users}*", parse_mode='Markdown')





        ###############################################################################обычные текст 2#############################################################################


@dp.message_handler(content_types=['text'])
async def get_message(message: types.Message):

    if message.text == "Пᴏᴧучиᴛь ᴄᴄыᴧᴋу💵":
        
        link = await get_start_link(str(message.from_user.username), encode=True)
        await bot.send_message(message.chat.id, text = f"*Ваша ссылка: {link} \n\nДля выхода команда: /menu 📴*", reply_markup=keyboard.dryg, parse_mode='Markdown')



    if message.text == "Пᴏᴄʍᴏᴛᴩᴇᴛь ᴩᴇɸᴇᴩᴀᴧᴏʙ🙋‍":
        await bot.send_message(message.chat.id, text = f"*___Данная система находится в тесте, только менеджер может посмотреть количество ваших рефералов🙋‍\n\n___Но вы можете посмотреть ВАШЕГО реферала, при команде (/start)*", reply_markup=keyboard.vash, parse_mode='Markdown')

    if message.text == "Назад🔹":
        await bot.send_message(message.chat.id, text= f"*Ты вернулся в главное меню👍\n\nдля помощи жми: /bothelp*", reply_markup=keyboard.start, parse_mode='Markdown')


    if message.text == "Дᴩуᴦᴏᴇ📚":
        await bot.send_message(message.chat.id, text= f"*В этом меню ты можешь: \n\n___Общаться онлайн с нашими клиентами \n<Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲>\n\n___Получить реферальную ссылку💵\n\n___Посмотреть ваших рефералов🙋‍\n\n___Посмотреть личный кабинет*", reply_markup=keyboard.other, parse_mode='Markdown')
    

        





    if message.text == "Ꮶᴧиᴇнᴛы ᴏнᴧᴀйн📲":
        await bot.send_message(message.chat.id, text= 'Ꮻнᴧᴀйн ᴄᴇйчᴀᴄ📲: ' + str(random.randint(10, 19)))

    if message.text == "Привет":
        await bot.send_message(message.chat.id, f"*Привет, {message.from_user.first_name}, я лучший бот - Авитолог👨‍💻.\n\nCмотри мои команды: /bothelp*", reply_markup=keyboard.start, parse_mode='Markdown')

    if message.text == "привет":
        await bot.send_message(message.chat.id, f"*Привет, {message.from_user.first_name}, я лучший бот - Авитолог👨‍💻.\n\nCмотри мои команды: /bothelp*", reply_markup=keyboard.start, parse_mode='Markdown')



    if message.text == "Ꮻᴛɜыʙы и Ꮯᴛᴀᴛиᴄᴛиᴋᴀ🕵️":
        await bot.send_message(message.chat.id, text = f"*Пᴩᴏᴄʍᴏᴛᴩ ᴏᴛɜыʙᴏʙ и ᴄᴛᴀᴛиᴄᴛиᴋи ᴏбьяʙᴧᴇний ᴋᴏʍᴨᴀнии📖:*", reply_markup=keyboard.stats, parse_mode='Markdown')

    if message.text == "Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ📈":
        await bot.send_message(message.chat.id, text = f"*Ᏼыбᴇᴩиᴛᴇ ᴄᴨᴇциᴀᴧиᴄᴛᴀ🤵:*", reply_markup=keyboard.razrab, parse_mode='Markdown')
        


    if message.text == "Ꮻᴨᴧᴀᴛᴀ💸":
        await bot.send_message(message.chat.id, text = f"*Ᏼыбᴇᴩиᴛᴇ удᴏбный ᴄᴨᴏᴄᴏб💳:*", reply_markup=keyboard.payment, parse_mode='Markdown')

    if message.text == "Пᴩᴀйᴄ-ᴧиᴄᴛ📃":
        await bot.send_message(message.chat.id, text = f"*Ᏼыбᴇᴩиᴛᴇ ᴛиᴨ ᴨᴧᴀнᴀ ᴨᴩᴏдʙижᴇния иᴧи ᴄᴏᴏбщиᴛᴇ ʍᴇнᴇджᴇᴩу \n(/manager) дᴧя индиʙидуᴀᴧьнᴏй ᴨᴩᴏᴦᴩᴀʍʍы📊:*", reply_markup=keyboard.price, parse_mode='Markdown')



    if message.text == "Адʍинᴄᴋиᴇ ᴋᴏнɸиᴦуᴩᴀции👩‍💻":
        await bot.send_message(message.chat.id, text = f"*Управляй ботом, Король, {message.from_user.first_name}!*", reply_markup=keyboard.static, parse_mode='Markdown')

    if message.text == "Измени новости🏪":
        await bot.send_message(message.chat.id, text = f"*Создай новость, Милорд, {message.from_user.first_name}! Команда: /me*", parse_mode='Markdown')

    if message.text == "Ꮋᴏʙᴏᴄᴛи🏪":
        link1 = open('link.txt', encoding="utf-8") # Вытаскиваем с нашей "БД" инфу, помещаем в переменную и выводим её
        link = link1.read()

        text1 = open('text.txt', encoding="utf-8") # Вытаскиваем с нашей "БД" инфу, помещаем в переменную и выводим её
        text = text1.read()

        await bot.send_message(message.chat.id, text = f"Свежая новость:\n\n{link}\n\n\n{text}", parse_mode='Markdown')


    if message.text == "Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲":
        await bot.send_message(message.chat.id, text = f"*Идет установка соединения...*", reply_markup=keyboard.connect, parse_mode='Markdown')
        await asyncio.sleep(5)
        await bot.send_message(message.chat.id, text = f"*Это может занять некоторое время...*", reply_markup=keyboard.connect, parse_mode='Markdown')
        await asyncio.sleep(5)
        await bot.send_message(message.chat.id, text = f"*Подготовка чата...*", reply_markup=keyboard.connect, parse_mode='Markdown')
        await asyncio.sleep(15)
        await bot.send_message(message.chat.id, text = f"*Серверу не удалось установить соединение...*", reply_markup=keyboard.connect, parse_mode='Markdown')
        await asyncio.sleep(1)
        await bot.send_message(message.chat.id, text = f"*Повторите попытку или вернитесь назад\n/menu*", reply_markup=keyboard.connect, parse_mode='Markdown')

    


   




    
    



        ############################################ОТЗЫВЫ############################################################################################################################

        



@dp.callback_query_handler(text_contains='join') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def join(callback: types.Message):
    await callback.message.answer(f'*Loading 1...*',  parse_mode='Markdown')
    await callback.message.answer('https://tgraph.io/file/0c2c94941cc6b33f23979.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/1213f10661f0935d50659.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/3decab2c5e39308d10ed0.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/83b1f92e2efbac47eb13a.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/d11138342d1870620796b.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/3c6d91cf352495c66a728.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/a79a4e1dcfa21ce5c4f32.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/0ca6e69b745469bc39466.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/efac0894d308aee835b5f.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/97f79722782807edaf367.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/1ea81d8d4b3658877a989.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/83b1f92e2efbac47eb13a.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/efac0894d308aee835b5f.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/0c2c94941cc6b33f23979.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://tgraph.io/file/3c6d91cf352495c66a728.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer(f'*Зᴀ дᴏᴨᴏᴧниᴛᴇᴧьныʍи ᴋᴇйᴄᴀʍи ᴏбᴩᴀᴛиᴛᴇᴄь ᴋ ᴋᴏнᴛᴇнᴛ-ʍᴇнᴇджᴇᴩу🤵 (https://t.me/tvoidrygim)...*', parse_mode='Markdown')
    await callback.answer()


@dp.callback_query_handler(text_contains='cancle') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def cancle(callback: types.Message):
    await callback.message.answer(f'*Loading 2...*',  parse_mode='Markdown')
    await asyncio.sleep(0.4)
    await callback.message.answer('Чᴛᴏбы ʙыбᴩᴀᴛь ᴋᴏнᴋуᴩᴇнᴛᴏᴄᴨᴏᴄᴏбную ниɯу, нужнᴏ иɜучиᴛь ᴨᴏᴛᴩᴇбнᴏᴄᴛи цᴇᴧᴇʙᴏй ᴀудиᴛᴏᴩии и ᴄᴨᴩᴏᴄ:\n'                                                                                                                                                                                                               
    '\n'
  '1.Зᴀйдиᴛᴇ ʙ ᴀнᴀᴧᴏᴦичныᴇ ᴏбъяʙᴧᴇния.📝\n' 
  '2.Ꮲᴀᴄᴄʍᴏᴛᴩиᴛᴇ, ᴋᴏᴦдᴀ ᴏбъяʙᴧᴇниᴇ ᴩᴀɜʍᴇщᴇнᴏ и ᴄᴋᴏᴧьᴋᴏ быᴧᴏ ᴨᴩᴏᴄʍᴏᴛᴩᴏʙ.🗠') 
    await asyncio.sleep(0.4)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615362043.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615362105.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('Ч⃨т⃨о⃨ п⃨о⃨м⃨о⃨ж⃨е⃨т⃨ с⃨д⃨е⃨л⃨а⃨т⃨ь⃨ о⃨б⃨ъя⃨в⃨л⃨е⃨н⃨и⃨е⃨ п⃨р⃨о⃨д⃨а⃨ю⃨щ⃨и⃨м⃨ ?\n'
    '\n'
'Чᴛᴏбы ᴏбъяʙᴧᴇниᴇ быᴧᴏ ᴨᴩᴏдᴀющиʍ, ᴏнᴏ дᴏᴧжнᴏ быᴛь ᴏᴩиᴇнᴛиᴩᴏʙᴀнныʍ нᴀ ᴨᴏᴛᴩᴇбнᴏᴄᴛи ᴋᴧиᴇнᴛᴀ, ᴨᴏᴋᴀɜыʙᴀᴛь, ᴋᴀᴋ ᴨᴩᴏдᴀʙᴀᴇʍᴀя ʙᴇщь иᴧи уᴄᴧуᴦᴀ ᴩᴇɯиᴛ ᴨᴩᴏбᴧᴇʍы ᴨᴏᴋуᴨᴀᴛᴇᴧя иᴧи уᴧучɯиᴛ ᴇᴦᴏ жиɜнь.\n'
    '\n'
             '*В⃨а⃨ж⃨н⃨ы⃨е⃨ а⃨с⃨п⃨е⃨к⃨т⃨ы⃨ п⃨р⃨и⃨ с⃨о⃨с⃨т⃨а⃨в⃨л⃨е⃨н⃨и⃨и⃨ о⃨б⃨ъя⃨в⃨л⃨е⃨н⃨и⃨й⃨⃨:*\n'
    '\n'
    '\n'
 '1...ᴋᴏнᴋᴩᴇᴛный и цᴇᴨᴧяющий ɜᴀᴦᴏᴧᴏʙᴏᴋ🗟;\n'
    '\n'
 '2...ɜᴀᴦᴏᴧᴏʙᴏᴋ ᴄᴏдᴇᴩжиᴛ ᴋᴧючᴇʙыᴇ ᴄᴧᴏʙᴀ\n' 
  '(ʙᴏᴄᴨᴏᴧьɜуйᴛᴇᴄь   Яндᴇᴋᴄ.Wᴏrdsᴛᴀᴛ иᴧи Gᴏᴏglᴇ Kᴇywᴏrd Plᴀnnᴇr\n'
            'дᴧя ᴏᴨᴩᴇдᴇᴧᴇния чᴀᴄᴛых\n' 
                      'ᴨᴏиᴄᴋᴏʙых ɜᴀᴨᴩᴏᴄᴏʙ ᴨᴏ ᴛᴇʍᴇ ʙᴀɯᴇᴦᴏ ᴛᴏʙᴀᴩᴀ)💬;\n'
    '\n'
 '3...ᴏᴨиᴄᴀниᴇ инᴛᴇᴩᴇᴄнᴏᴇ, нᴇ ᴏᴄᴛᴀʙᴧяᴇᴛ ᴨᴏᴄᴧᴇ ᴄᴇбя   ʙᴏᴨᴩᴏᴄᴏʙ🙋;\n'
 '\n'
 '4...ᴏᴨиᴄᴀниᴇ ᴋᴩᴀᴛᴋᴏᴇ нᴀ чᴛᴇниᴇ нᴇ ухᴏдиᴛ бᴏᴧᴇᴇ 2-3 ʍинуᴛ📃;\n'
 '\n'
 '5...ᴏᴨиᴄᴀниᴇ ᴄᴏдᴇᴩжиᴛ ᴋᴩиᴛичныᴇ дᴧя ᴨᴏᴋуᴨᴀᴛᴇᴧя\n'
           'хᴀᴩᴀᴋᴛᴇᴩиᴄᴛиᴋи (ᴩᴀɜʍᴇᴩ, ᴩᴏᴄᴛ ᴨᴏᴛᴇнциᴀᴧьнᴏᴦᴏ\n'
                      'ᴨᴏᴋуᴨᴀᴛᴇᴧя)📊;\n')
    await asyncio.sleep(0.4)

    await callback.message.answer('https://partnerkin.com/storage/files/file_1615362347.jpg')
    await asyncio.sleep(0.4)
    
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615362387.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('*е͟͟с͟͟т͟͟ь͟͟ и͟͟н͟͟ф͟͟о͟͟р͟͟м͟͟а͟͟ц͟͟и͟͟я͟͟, д͟͟л͟͟я͟͟ ч͟͟е͟͟г͟͟о͟͟ т͟͟о͟͟в͟͟а͟͟р͟͟ п͟͟о͟͟д͟͟х͟͟о͟͟д͟͟и͟͟т͟͟, к͟͟а͟͟к͟͟у͟͟ю͟͟ п͟͟р͟͟о͟͟б͟͟л͟͟е͟͟м͟͟у͟͟ р͟͟е͟͟ш͟͟а͟͟е͟͟т͟͟:*\n'
        '\n'
        '\n'
        '\n'
        '1...ɸᴏᴛᴏᴦᴩᴀɸии хᴏᴩᴏɯᴇᴦᴏ ᴋᴀчᴇᴄᴛʙᴀ, ᴨᴏᴋᴀɜыʙᴀюᴛ,📸\n'
            'ᴋᴀᴋ ʙыᴦᴧядиᴛ ᴛᴏʙᴀᴩ ᴄᴨᴇᴩᴇди, ᴄбᴏᴋу, ᴄɜᴀди,\n'
               'нᴀ ʍᴏдᴇᴧи (ᴇᴄᴧи ϶ᴛᴏ ᴏдᴇждᴀ),\n'
                  'ᴋᴀᴋиᴇ ᴇᴄᴛь ʙᴀжныᴇ дᴇᴛᴀᴧи ᴛᴏʙᴀᴩᴀ\n'
                     '(уʙᴇᴧичᴇнныᴇ ᴋᴀдᴩы);  ᴋᴏнᴛᴀᴋᴛы ᴀᴋᴛуᴀᴧьны,\n'
                         'ᴀдᴩᴇᴄ и ᴄхᴇʍᴀ ᴨᴩᴏᴇɜдᴀ ᴨᴏняᴛнᴀ(ʙᴀɯ ʍᴀᴦᴀɜин);\n'
        '\n'
        '\n'
        '2...ᴇᴄᴛь ʙидᴇᴏᴋᴏнᴛᴇнᴛ, ᴩᴀᴄᴄᴋᴀɜыʙᴀющий ᴏ ᴨᴩᴏдᴀʙᴀᴇʍᴏй ʙᴇщи:\n'
            '϶ᴛᴏ ʙыᴦᴏднᴏ ᴏᴛᴄᴛᴩᴏиᴛ ʙᴀɯ ᴛᴏʙᴀᴩ ᴏᴛ ᴋᴏнᴋуᴩᴇнᴛᴏʙ\n'
                'и ɜᴀʍᴏᴛиʙиᴩуᴇᴛ цᴇᴧᴇʙую ᴀудиᴛᴏᴩию, ᴨᴩᴇдᴨᴏчиᴛᴀющую\n'
                 'ʙиɜуᴀᴧьныᴇ ᴋᴀнᴀᴧы ʙᴏᴄᴨᴩияᴛия инɸᴏᴩʍᴀции;\n'
                 '\n'
        '\n'
        '3...Кᴏʍᴨᴀния Aʍᴀzᴏn ᴨᴩᴏʙᴏдиᴧᴀ иᴄᴄᴧᴇдᴏʙᴀния,🎞\n'
           'ʙ хᴏдᴇ ᴋᴏᴛᴏᴩых ʙыяᴄниᴧᴏᴄь, чᴛᴏ нᴀ ᴄᴛᴩᴀницы ᴛᴏʙᴀᴩᴏʙ\n'
              'ᴄ ʙидᴇᴏ ᴋᴧиᴇнᴛы ɜᴀхᴏдяᴛ чᴀщᴇ.\n'
              '\n'
        '\n'
        '4...Оптиmально указать причину продажи или ⚠️\n'
            'чeстную историю товара, чтобы повысить довeриe покупатeлeй.\n' )
    await asyncio.sleep(0.4)
        
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615362449.gif')
    await asyncio.sleep(0.4)
    await callback.message.answer('О͟͟п͟͟т͟͟о͟͟в͟͟а͟͟я͟͟ п͟͟р͟͟о͟͟д͟͟а͟͟ж͟͟а͟͟🗞')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615364616.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615364641.jpg')
    await asyncio.sleep(0.4)
    await callback.message.answer('https://partnerkin.com/storage/files/file_1615364548.jpg')

    
    await callback.answer()




@dp.callback_query_handler(text_contains='cancl') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def cancl(callback: types.Message):
    await callback.message.answer('Выполненных заказов: 453\n\n'
        'В работе: 36\n\n'
        'Всего: 489\n\n'
        '\n'
        'Обновлено cекунд назад: '+ str(random.randint(1, 10)))

    
    await callback.answer()  

@dp.callback_query_handler(text_contains='can') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def can(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text= f"*Ты вернулся в главное меню. \n\n\nЖми: /keys*", parse_mode='Markdown')
       

    






    ############################################ОПЛАТА############################################################################################################################




@dp.callback_query_handler(text_contains='Jove') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def Jove(callback: types.CallbackQuery):
    await callback.message.answer('https://qiwi.com/payment/form/99')
    await callback.answer()
    
       
       
    



@dp.callback_query_handler(text_contains='canceel') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def canceel(callback: types.CallbackQuery):
    await callback.message.answer('text 1')
    await callback.answer()    






    ###########################################################МЕНЕДЖМЕНТ##################################################################################








@dp.callback_query_handler(text_contains='content') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def content(callback: types.CallbackQuery):
    await callback.message.answer('https://t.me/tvoidrygim')
    await callback.answer()
    
       
       
    



@dp.callback_query_handler(text_contains='audit') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def audit(callback: types.CallbackQuery):
    await callback.message.answer('https://t.me/tvoidrygim')
    await callback.answer()    



@dp.callback_query_handler(text_contains='podder') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def podder(callback: types.CallbackQuery):
    await callback.message.answer('https://t.me/tvoidrygim')
    await callback.answer()



#######################################################################ПРАЙС ЛИСТ########################################################


@dp.callback_query_handler(text_contains='priceone') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def priceone(callback: types.CallbackQuery):
    await callback.message.answer('text 2')
    await callback.answer()



@dp.callback_query_handler(text_contains='pricetwo') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def pricetwo(callback: types.CallbackQuery):
    await callback.message.answer('text 2')
    await callback.answer()


@dp.callback_query_handler(text_contains='pricetree') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def pricetree(callback: types.CallbackQuery):
    await callback.message.answer('text 2')
    await callback.answer()


############################################################################Админское меню#######################################################

@dp.callback_query_handler(text_contains='adminone') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def adminone(call: types.CallbackQuery):
    if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"*Вот статистика, Император, {message.from_user.first_name}: \n*{d}* человек*", parse_mode='Markdown')
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = "*У тебя нет админки, увы...😪*", parse_mode='Markdown')


@dp.callback_query_handler(text_contains='admintwo') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def admintwo(callback: types.CallbackQuery):
    await callback.message.answer(f"Команда для рассылки: \n/rassilka текст рассылки")
    await callback.answer()

























    ##############################################################
if __name__ == '__main__':
    print('Монстр пчелы запущен!')                                    # ЧТОБЫ БОТ РАБОТАЛ ВСЕГДА с выводом в начале вашего любого текста
executor.start_polling(dp)
##############################################################







