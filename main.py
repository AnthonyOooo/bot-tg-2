# -*- coding: utf8 -*-




#╔═══╗───╔╗──╔╗──────╔════╗────────────╔╗
#║╔══╝───║╚╗╔╝║──────║╔╗╔╗║───────────╔╝╚╗
#║╚══╗╔═╗╚╗║║╔╝╔╗╔═╗─╚╝║║╚╝╔═╗╔══╗╔══╗╚╗╔╝
#║╔══╝║╔╝─║╚╝║─╠╣║╔╗╗──║║──║╔╝║╔╗║║╔═╝─║║
#║╚══╗║║──╚╗╔╝─║║║║║║──║║──║║─║╔╗║║╚═╗─║╚╗
#╚═══╝╚╝───╚╝──╚╝╚╝╚╝──╚╝──╚╝─╚╝╚╝╚══╝─╚═╝



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

#######################

import sqlite3
from sqlite3 import Error
from time import sleep, ctime



def post_sql_query(sql_query):
    with sqlite3.connect('ref.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
            connection.commit()
        except Exception as e:
            print(e)
        result = cursor.fetchall()
        return result

def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS users 
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        refer INTEGER);'''
    post_sql_query(users_query)

def register_user(user, refer):
    user_check_query = f'SELECT * FROM users WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO users VALUES ({user}, {refer});'
        post_sql_query(insert_to_db_query )

create_tables()

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


@dp.message_handler(Command("bots"), state=None)

async def bots(message):
    await bot.send_message(message.chat.id, f"*🥺*",  reply_markup=keyboard.bots, parse_mode='Markdown')


@dp.message_handler(Command("pakets"), state=None)

async def pakets(message):
    await bot.send_message(message.chat.id, f"*🥺*",  reply_markup=keyboard.pakets, parse_mode='Markdown')


@dp.message_handler(Command("keys"), state=None)

async def keys(message):
    await bot.send_message(message.chat.id, f"*Клавиатура открыта ⌨️*",  reply_markup=keyboard.keys, parse_mode='Markdown')

@dp.message_handler(Command("ref"), state=None)

async def ref(message):
    await bot.send_message(message.chat.id, f"*За КАЖДОГО приглашенного друга приятная скидка на услуги:)*", reply_markup=keyboard.ref, parse_mode='Markdown')
    args = message.get_args()
    try:
        refer = post_sql_query(f"SELECT * FROM users WHERE user_id = {message.from_user.id}")[0][1]
    except:
        refer = 0
    if refer != 0:
        reference = post_sql_query(f"SELECT user_id FROM users WHERE user_id = {refer}")
    else:
        reference = 'Пусто'

    await message.answer(f"*Ваш рефер: {reference}*", reply_markup=keyboard.ref, parse_mode='Markdown') #здесь в  reference должен быть юзернейм, того кто создал ссылку


@dp.message_handler(Command("pack"), state=None)

async def pack(message):
    await bot.send_message(message.chat.id, f"*Наша статистика за последние 2 месяца 📊*",  reply_markup=keyboard.pack, parse_mode='Markdown')


@dp.message_handler(Command("manager"), state=None)

async def manager(message):
    await bot.send_message(message.chat.id, f"*Для связи с менеджером жми кнопку🤖*",  reply_markup=keyboard.manager, parse_mode='Markdown')


@dp.message_handler(Command("done"), state=None)

async def done(message):
    await bot.send_message(message.chat.id, f"*Наша статистика за последние 2 месяца📊*",  reply_markup=keyboard.done, parse_mode='Markdown')



@dp.message_handler(Command("pay"), state=None)

async def pay(message):
    await bot.send_message(message.chat.id, f"*Для оплаты выбери нужную услугу*",  reply_markup=keyboard.pay, parse_mode='Markdown')

@dp.message_handler(Command("prt"), state=None)

async def prt(message):
    await bot.send_message(message.chat.id, f"*Уточните номер пакета:*",  reply_markup=keyboard.prt, parse_mode='Markdown')





@dp.message_handler(Command("menu"), state=None)

async def menu(message):
    await bot.send_message(message.chat.id, f"*Если заблудился:) \n\nВсегда есть команда: /bothelp 📖*",  reply_markup=keyboard.menu, parse_mode='Markdown')


@dp.message_handler(Command("connect"), state=None)

async def connect(message):
    await bot.send_message(message.chat.id, f"*Нажми <Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲>*",  reply_markup=keyboard.connect, parse_mode='Markdown')



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



@dp.message_handler(commands=['start'])
async def start(message):
    try:
        refer = int(message.text[7:])
    except Exception as e:
        refer = 0
    if refer:
        if type(refer) == int:
            if int(refer) != message.from_user.id:
                try:
                    refer2 = post_sql_query(f'SELECT * FROM users WHERE user_id = {refer}')[0][0]
                    if refer2:
                        register_user(message.from_user.id, refer)

                        await bot.send_message(refer, 'По вашей ссылке перешёл <a href="tg://user?id={}">реферал</a>', parse_mode='html')


                except Exception as e:
                    register_user(message.from_user.id, 0)
            else:
                register_user(message.from_user.id, 0)
        else:
            register_user(message.from_user.id, 0)
    else:
        register_user(message.from_user.id, 0)

    joinedFile = open("user.txt","r")
    joinedUsers = set ()
    for line in joinedFile:
        joinedUsers.add(line.strip())

    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("user.txt","a")
        joinedFile.write(str(message.chat.id)+ "\n")
        joinedUsers.add(message.chat.id)


    await bot.send_message(message.chat.id, f"*❗️ Привет, я — бот Авитолог, созданный для  твоего продвижения на авито:) \n\nЯ предлагаю тебе выгодные условия для продвижения, показываю результаты заказов и статистику нашей команды, предлагаю пакеты услуг📋. \n\nВсе просто: \n ___Приводи друзей в бота и получай скидку за КАЖДОГО друга в (/ref)💵💵\n___Выбирай услугу, в <Пᴩᴀйᴄ-ᴧиᴄᴛ📃> (/pack), запоминай номер \n ___Далее нажимай кнопку: <Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈> (/manager ) \n___Говори номер услуги, или просто спроси про свою нишу и условия \n___Так же можешь оплатить услугу тут в <Ꮻᴨᴧᴀᴛᴀ💸>(/pay), ❗️главное  указать комментраий и цену 1в1 ❗️ \n___Смотри наши выполненные заказы (/done) \n___Получи своего бесплатного бота в телеграм, просто напиши менеджеру(/meneger) ✅ \n___Наши клиенты имеют постоянные скидки на следующие заказы, нас выбирают именно за качество выполнения заказов, а так же наша команда самая ответственная и дружелюбна на рынке, присоединяйся❗️ \n\n\nОсновные команды: \n/start - Перезапустить бота🔁 \n/ref - Реферальная система🕺\n/keys - Вводи в любой непонятной ситуации🗿 \n/bothelp - Откроет это окно🧾 \n/menu - Открывает нижнее меню💻 \n/connect - Общение между клиентами👩‍💻 \n/manager - Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈 \n/pack - Пᴩᴀйᴄ-ᴧиᴄᴛ📃 \n/pay - Ꮻᴨᴧᴀᴛᴀ💸\n/done - Выполненные заказы✅\n/bots - Бᴇᴄᴨᴧᴀᴛный бᴏᴛ🤖*", reply_markup=keyboard.start, parse_mode='Markdown')
   


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
                await bot.send_message(user, message.text[message.text.find(' '):])
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
        
        link = await get_start_link(message.from_user.id, encode=False)
        await bot.send_message(message.chat.id, text = f'Ваша ссылка: {link} \n\nУзнайте скидку у <a href="https://t.me/tvoidrygim">вашего менеджера🤵</a>', reply_markup=keyboard.dryg, parse_mode='html', disable_web_page_preview=1)



    if message.text == "Пᴏᴄʍᴏᴛᴩᴇᴛь ᴩᴇɸᴇᴩᴀᴧᴏʙ🙋‍":
        try:
            referals_id = post_sql_query(f"SELECT * FROM users WHERE refer = {message.from_user.id}")
            msg = "Список рефералов по айди: \n\n"
            if len(referals_id) != 0:
                if len(referals_id) >= 50:
                    b = 0
                    for i in referals_id:
                        if int(b) == 0:
                            msg += ("<b>—</b> " + "<a href='tg://user?id=" + "".join(str(i[0])) + "'>" + "".join(str(i[0])) + "</a>  ")
                            b = 1
                        else:
                            msg += ("<b>—</b> " + "<a href='tg://user?id=" + "".join(str(i[0])) + "'>" + "".join(str(i[0])) + "</a>\n")
                            b = 0
                else:
                    for i in referals_id:
                        msg += ("<b>—</b> " + "<a href='tg://user?id=" + "".join(str(i[0])) + "'>" + "".join(str(i[0])) + "</a>\n")

                msg += ("\n<i>Если вы хотите посмотреть их профиль то нажмите на id !</i>")
            else:
                msg += ("<b>—</b> " + "<i>Увы, вы ещё никого не пригласили :(</i>\n")

            await message.answer(msg, parse_mode='html')
        except Exception as e:
            print(e)
        

    if message.text == "Назад🔹":
        await bot.send_message(message.chat.id, text= f"*Ты вернулся в главное меню🖱*", reply_markup=keyboard.start, parse_mode='Markdown')


    if message.text == "Дᴩуᴦᴏᴇ📚":
        await bot.send_message(message.chat.id, text= f"*В этом меню ты можешь: \n\n___Общаться онлайн с нашими клиентами \n        <Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲>\n\n___Получить реферальную ссылку💵\n\n___Посмотреть ваших рефералов🙋‍*", reply_markup=keyboard.other, parse_mode='Markdown')
    

        





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
        await bot.send_message(message.chat.id, text = f"*Ᏼыбᴇᴩиᴛᴇ уᴄᴧуᴦу📑:*", reply_markup=keyboard.payment, parse_mode='Markdown')

    if message.text == "Пᴩᴀйᴄ-ᴧиᴄᴛ📃":
        await bot.send_message(message.chat.id, text = f'Ᏼыбᴇᴩиᴛᴇ ᴛиᴨ ᴨᴧᴀнᴀ ᴨᴩᴏдʙижᴇния иᴧи ᴄᴏᴏбщиᴛᴇ <a href="https://t.me/Avito1log">ʍᴇнᴇджᴇᴩу</a> дᴧя индиʙидуᴀᴧьнᴏй ᴨᴩᴏᴦᴩᴀʍʍы📊:', reply_markup=keyboard.price, parse_mode='html', disable_web_page_preview=1)



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

    

    if message.text == "Пакет 1 🛍":
        await bot.send_message(message.chat.id, text = f'📃 №1:  Авито услуги (100 объявлений, с кураторством 30 дней)\n\n💰 Цена: 15000 ₽ \n(оплатить 50% от суммы, остальное после выполнения заказа)\n\n📃 Описание: Мы размещаем объявления в вашей нише в течении 30 дней с полным анализом ниши, и подборкой стратегии размещения.\n\nС вами свяжется менеджер после покупки, после оплаты сделайте скриншот, для ускорения проверки, пришлите его <a href="https://t.me/Avito1log">менеджеру(жми)</a>\n\n📦 Кол-во: 1 шт.\n➖➖➖➖➖➖➖➖➖➖➖➖\n💡 Заказ #4189150\n🕐 Итоговая сумма: 7500 ₽  (Личная скидка 0 %)\n➖➖➖➖➖➖➖➖➖➖➖➖\n☎️ Кошелек для оплаты: <a href="https://oplata.qiwi.com/form?invoiceUid=ee0cd87f-959e-47ea-9f33-0ac83ebca28a">Готовая ссылка (жми)</a>  \n💰 Сумма: 7500 ₽\n💭 Комментарий: 4189150\nВАЖНО: Комментарий и сумма должны быть 1в1\n➖➖➖➖➖➖➖➖➖➖➖➖\n⏰ Время на оплату: 15 минут', reply_markup=keyboard.one, parse_mode='html', disable_web_page_preview=1)

    if message.text == "Пакет 2 🛍":
        await bot.send_message(message.chat.id, text = f'📃 №2:  Авито услуги (200 объявлений, с кураторством 30 дней)\n\n💰 Цена: 20400 ₽ \n(оплатить 50% от суммы, остальное после выполнения заказа)\n\n📃 Описание: Мы размещаем объявления в вашей нише в течении 30 дней с полным анализом ниши, и подборкой стратегии размещения.\n\nС вами свяжется менеджер после покупки, после оплаты сделайте скриншот, для ускорения проверки, пришлите его <a href="https://t.me/Avito1log">менеджеру(жми)</a>\n\n📦 Кол-во: 1 шт.\n➖➖➖➖➖➖➖➖➖➖➖➖\n💡 Заказ #4189151\n🕐 Итоговая сумма: 10200 ₽  (Личная скидка 0 %)\n➖➖➖➖➖➖➖➖➖➖➖➖\n☎️ Кошелек для оплаты: <a href="https://oplata.qiwi.com/form?invoiceUid=17b22ebb-9f4d-4567-b7b7-114a8ab830d7">Готовая ссылка (жми)</a> \n💰 Сумма: 10200 ₽\n💭 Комментарий: 4189151\nВАЖНО: Комментарий и сумма должны быть 1в1\n➖➖➖➖➖➖➖➖➖➖➖➖\n⏰ Время на оплату: 15 минут', reply_markup=keyboard.two, parse_mode='html', disable_web_page_preview=1)

    if message.text == "Пакет 3 🛍":
        await bot.send_message(message.chat.id, text = f'📃 №3:  Авито услуги (300 объявлений, с кураторством 30 дней)\n\n💰 Цена: 25600 ₽ \n(оплатить 50% от суммы, остальное после выполнения заказа)\n\n📃 Описание: Мы размещаем объявления в вашей нише в течении 30 дней с полным анализом ниши, и подборкой стратегии размещения.\n\nС вами свяжется менеджер после покупки, после оплаты сделайте скриншот, для ускорения проверки, пришлите его <a href="https://t.me/Avito1log">менеджеру(жми)</a>\n\n📦 Кол-во: 1 шт.\n➖➖➖➖➖➖➖➖➖➖➖➖\n💡 Заказ #4189152\n🕐 Итоговая сумма: 12800 ₽  (Личная скидка 0 %)\n➖➖➖➖➖➖➖➖➖➖➖➖\n☎️ Кошелек для оплаты: <a href="https://oplata.qiwi.com/form?invoiceUid=1414e876-0f4b-4952-8bbb-df6a30d1e03f">Готовая ссылка (жми)</a>\n💰 Сумма: 12800 ₽\n💭 Комментарий: 4189152\nВАЖНО: Комментарий и сумма должны быть 1в1\n➖➖➖➖➖➖➖➖➖➖➖➖\n⏰ Время на оплату: 15 минут', reply_markup=keyboard.tree, parse_mode='html', disable_web_page_preview=1)

    if message.text == "Пакет 4 🛍":
        await bot.send_message(message.chat.id, text = f'📃 №4:  Авито услуги (400 объявлений, с кураторством 30 дней)\n\n💰 Цена: 31200 ₽ \n(оплатить 50% от суммы, остальное после выполнения заказа)\n\n📃 Описание: Мы размещаем объявления в вашей нише в течении 30 дней с полным анализом ниши, и подборкой стратегии размещения.\n\nС вами свяжется менеджер после покупки, после оплаты сделайте скриншот, для ускорения проверки, пришлите его <a href="https://t.me/Avito1log">менеджеру(жми)</a>\n\n📦 Кол-во: 1 шт.\n➖➖➖➖➖➖➖➖➖➖➖➖\n💡 Заказ #4189153\n🕐 Итоговая сумма: 15600 ₽  (Личная скидка 0 %)\n➖➖➖➖➖➖➖➖➖➖➖➖\n☎️ Кошелек для оплаты: <a href="https://oplata.qiwi.com/form?invoiceUid=4b49f178-02a2-415a-9511-6ef913918295">Готовая ссылка (жми)</a>\n💰 Сумма: 15600 ₽\n💭 Комментарий: 4189153\nВАЖНО: Комментарий и сумма должны быть 1в1\n➖➖➖➖➖➖➖➖➖➖➖➖\n⏰ Время на оплату: 15 минут', reply_markup=keyboard.fo, parse_mode='html', disable_web_page_preview=1)

    if message.text == "Пакет 5 🛍":
        await bot.send_message(message.chat.id, text = f'📃 №5:  Авито услуги (500 объявлений, с кураторством 30 дней)\n\n💰 Цена: 37800 ₽ \n(оплатить 50% от суммы, остальное после выполнения заказа)\n\n📃 Описание: Мы размещаем объявления в вашей нише в течении 30 дней с полным анализом ниши, и подборкой стратегии размещения.\n\nС вами свяжется менеджер после покупки, после оплаты сделайте скриншот, для ускорения проверки, пришлите его <a href="https://t.me/Avito1log">менеджеру(жми)</a>\n\n📦 Кол-во: 1 шт.\n➖➖➖➖➖➖➖➖➖➖➖➖\n💡 Заказ #4189154\n🕐 Итоговая сумма: 18900 ₽  (Личная скидка 0 %)\n➖➖➖➖➖➖➖➖➖➖➖➖\n☎️ Кошелек для оплаты: <a href="https://oplata.qiwi.com/form?invoiceUid=0df3a301-6a74-44ee-82d6-223f49ead6bd">Готовая ссылка (жми)</a>\n💰 Сумма: 18900 ₽\n💭 Комментарий: 4189154\nВАЖНО: Комментарий и сумма должны быть 1в1\n➖➖➖➖➖➖➖➖➖➖➖➖\n⏰ Время на оплату: 15 минут', reply_markup=keyboard.five, parse_mode='html', disable_web_page_preview=1)
    
    if message.text == "Пакет 6 🛍":
        await bot.send_message(message.chat.id, text = f'📃 №6:  Авито услуги (600 объявлений, с кураторством 30 дней)\n\n💰 Цена: 44400 ₽ \n(оплатить 50% от суммы, остальное после выполнения заказа)\n\n📃 Описание: Мы размещаем объявления в вашей нише в течении 30 дней с полным анализом ниши, и подборкой стратегии размещения.\n\nС вами свяжется менеджер после покупки, после оплаты сделайте скриншот, для ускорения проверки, пришлите его <a href="https://t.me/Avito1log">менеджеру(жми)</a>\n\n📦 Кол-во: 1 шт.\n➖➖➖➖➖➖➖➖➖➖➖➖\n💡 Заказ #4189155\n🕐 Итоговая сумма: 22200 ₽  (Личная скидка 0 %)\n➖➖➖➖➖➖➖➖➖➖➖➖\n☎️ Кошелек для оплаты: <a href="https://oplata.qiwi.com/form?invoiceUid=f0cee479-f6d7-44d9-8fa8-79c6418cb273">Готовая ссылка (жми)</a>\n💰 Сумма: 22200 ₽\n💭 Комментарий: 4189155\nВАЖНО: Комментарий и сумма должны быть 1в1\n➖➖➖➖➖➖➖➖➖➖➖➖\n⏰ Время на оплату: 15 минут', reply_markup=keyboard.six, parse_mode='html', disable_web_page_preview=1)


    if message.text == "Все пакеты 🛍":
        await bot.send_message(message.chat.id, text = f"📌ВАЖНО!\nПомимо постинга на Авито и Юле, оказываем услуги:\n🔹 Парсинг телефонов с Авито и Юлы (все категории)\n🔹 Парсинг объявлений Авито (все категории)\n🔹 Парсинг объявлений Юлы (все категории)\n🔹 Парсинг по поисковому запросу на Авито и Юле\n🔹 Парсинг аккаунта/магазина на Авито и Юле\n🔹 Парсинг по нужным датам\n🔹Автопарсинг по поисковому\n      запросу на Авито (выгружаются \n      все новые объявления)\n🔹 Возможность собирать только \n      уникальные телефоны\n\n📌Прайс:\n🔹 до 100 - 200 руб.\n🔹 до 500 - 400 руб.\n🔹 до 1000 - 600 руб.\n🔹 до 1500 - 900 руб.\n🔹 до 2000 - 1200 руб\n🔹 до 3000 - 1500 руб.\n🔹 до 4000 - 1800 руб.\n🔹 до 5000 - 2000 руб.\n🔹 Более 5000 - цена \n      индивидуальна.\n🔹Автопарсинг по поисковому \n      запросу - цена индивидуальна., \n      пиши - <a href='https://t.me/Avito1log'>менеджеру(жми)</a>", reply_markup=keyboard.pars, parse_mode='html', disable_web_page_preview=1)


    if message.text == "Зᴀᴋᴀɜᴀᴛь бᴏᴛᴀ дᴧя биɜнᴇᴄᴀ 🏭":
        await bot.send_message(message.chat.id, text = f'Только личная консультация - <a href="https://t.me/Avito1log">(жми)</a>🙎‍', reply_markup=keyboard.bibo, parse_mode='html', disable_web_page_preview=1)

    if message.text == "Зᴀбᴇᴩи ᴄʙᴏᴇᴦᴏ бᴏᴛᴀ🤖":
        await bot.send_message(message.chat.id, text = f'Чтобы забрать бесплатного бота напиши <a href="https://t.me/Avito1log">менеджеру</a> твой личный сгенерированный код(53QTE) 🤖\n\n', reply_markup=keyboard.bibo, parse_mode='html', disable_web_page_preview=1)

    


   




    
    



        ############################################ОТЗЫВЫ############################################################################################################################

        



@dp.callback_query_handler(text_contains='join') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def join(callback: types.Message):
    await callback.message.answer(f'*Loading 1...*',  parse_mode='Markdown')
    await callback.message.answer('<a href="https://tgraph.io/file/0c2c94941cc6b33f23979.jpg">Наш кейс</a>', parse_mode='html')
   
    await callback.message.answer('<a href="https://tgraph.io/file/1213f10661f0935d50659.jpg">Наш кейс</a>', parse_mode='html')
 
    await callback.message.answer('<a href="https://tgraph.io/file/3decab2c5e39308d10ed0.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/83b1f92e2efbac47eb13a.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/d11138342d1870620796b.jpg">Наш кейс</a>', parse_mode='html')
   
    await callback.message.answer('<a href="https://tgraph.io/file/3c6d91cf352495c66a728.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/a79a4e1dcfa21ce5c4f32.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/0ca6e69b745469bc39466.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/efac0894d308aee835b5f.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/97f79722782807edaf367.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/1ea81d8d4b3658877a989.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/83b1f92e2efbac47eb13a.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://tgraph.io/file/efac0894d308aee835b5f.jpg">Наш кейс</a>', parse_mode='html')
 
    await callback.message.answer('<a href="https://tgraph.io/file/0c2c94941cc6b33f23979.jpg">Наш кейс</a>', parse_mode='html')
   
    await callback.message.answer('<a href="https://tgraph.io/file/3c6d91cf352495c66a728.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('Зᴀ дᴏᴨᴏᴧниᴛᴇᴧьныʍи ᴋᴇйᴄᴀʍи ᴏбᴩᴀᴛиᴛᴇᴄь ᴋ <a href="https://t.me/Avito1log">кᴏнᴛᴇнᴛ-ʍᴇнᴇджᴇᴩу🤵</a>', parse_mode='html', disable_web_page_preview=1)
    await callback.answer()


@dp.callback_query_handler(text_contains='cancle') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def cancle(callback: types.Message):
    await callback.message.answer(f'*Loading 2...*',  parse_mode='Markdown')
    
    await callback.message.answer('Чᴛᴏбы ʙыбᴩᴀᴛь ᴋᴏнᴋуᴩᴇнᴛᴏᴄᴨᴏᴄᴏбную ниɯу, нужнᴏ иɜучиᴛь ᴨᴏᴛᴩᴇбнᴏᴄᴛи цᴇᴧᴇʙᴏй ᴀудиᴛᴏᴩии и ᴄᴨᴩᴏᴄ:\n'                                                                                                                                                                                                               
    '\n'
  '1.Зᴀйдиᴛᴇ ʙ ᴀнᴀᴧᴏᴦичныᴇ ᴏбъяʙᴧᴇния.📝\n' 
  '2.Ꮲᴀᴄᴄʍᴏᴛᴩиᴛᴇ, ᴋᴏᴦдᴀ ᴏбъяʙᴧᴇниᴇ ᴩᴀɜʍᴇщᴇнᴏ и ᴄᴋᴏᴧьᴋᴏ быᴧᴏ ᴨᴩᴏᴄʍᴏᴛᴩᴏʙ.🗠') 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615362043.jpg">Наш кейс</a>', parse_mode='html')
    
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615362105.jpg">Наш кейс</a>', parse_mode='html')
    
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
    

    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615362347.jpg">Наш кейс</a>', parse_mode='html')
   
    
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615362387.jpg">Наш кейс</a>', parse_mode='html')
   
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

        
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615362449.gif">Наш кейс</a>', parse_mode='html')

    await callback.message.answer('О͟͟п͟͟т͟͟о͟͟в͟͟а͟͟я͟͟ п͟͟р͟͟о͟͟д͟͟а͟͟ж͟͟а͟͟🗞')
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615364616.jpg">Наш кейс</a>', parse_mode='html')
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615364641.jpg">Наш кейс</a>', parse_mode='html')
    await callback.message.answer('<a href="https://partnerkin.com/storage/files/file_1615364548.jpg">Наш кейс</a>', parse_mode='html')

    
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
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text= f"*Ты вернулся в главное меню👍*", parse_mode='Markdown')
       

    






    ############################################ОПЛАТА############################################################################################################################




@dp.callback_query_handler(text_contains='Jove') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def Jove(callback: types.CallbackQuery):
    await callback.message.answer(text = f"*📃 Уточните номер пакета:*" ,reply_markup=keyboard.pakets, parse_mode='Markdown')
    await callback.answer()
    










       
       
    



@dp.callback_query_handler(text_contains='vroom') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def vroom(callback: types.CallbackQuery):
    await callback.message.answer(text = f'*📃 Уточните номер пакета:*',reply_markup=keyboard.prt, parse_mode='Markdown')
    await callback.answer() 


@dp.callback_query_handler(text_contains='hou') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def hou(callback: types.CallbackQuery):
    await callback.message.answer(text = f'*📃 Уточните номер пакета:*',reply_markup=keyboard.bots, parse_mode='Markdown')
    await callback.answer()      






    ###########################################################МЕНЕДЖМЕНТ##################################################################################








@dp.callback_query_handler(text_contains='content') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def content(callback: types.CallbackQuery):
    await callback.message.answer(text = f'Уᴨᴩᴀʙᴧяющий ᴄᴨᴇциᴀᴧиᴄᴛ - <a href="https://t.me/Avito1log">Ꮶᴏнᴛᴇнᴛ-ʍᴇнᴇджᴇᴩ👨‍🏫(Жʍи)</a>', parse_mode='html', disable_web_page_preview=1)
    await callback.answer()
    
       
       
    



@dp.callback_query_handler(text_contains='audit') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def audit(callback: types.CallbackQuery):
    await callback.message.answer(text = f'Бᴇᴄᴨᴧᴀᴛный ᴀудиᴛ - <a href="https://t.me/Avito1log">(Жʍи)</a>', parse_mode='html', disable_web_page_preview=1)
    await callback.answer()    



@dp.callback_query_handler(text_contains='podder') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def podder(callback: types.CallbackQuery):
    await callback.message.answer(text = f'Пᴏ ᴏᴄᴛᴀᴧьныʍ ʙᴏᴨᴩᴏᴄᴀʍ - <a href="https://t.me/Avito1log">Ꭲᴇх.Пᴏддᴇᴩжᴋᴀ(Жʍи)👩‍💻</a>', parse_mode='html', disable_web_page_preview=1)
    await callback.answer()



#######################################################################ПРАЙС ЛИСТ########################################################


@dp.callback_query_handler(text_contains='priceone') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def priceone(callback: types.CallbackQuery):
    await callback.message.answer(text = f"*📃 Уточните номер пакета:*" ,reply_markup=keyboard.pakets, parse_mode='Markdown')
    await callback.answer()



@dp.callback_query_handler(text_contains='pricetwo') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def pricetwo(callback: types.CallbackQuery):
    await callback.message.answer(text = f'*📃 Уточните номер пакета:*',reply_markup=keyboard.prt, parse_mode='Markdown')
    await callback.answer()


@dp.callback_query_handler(text_contains='pricetree') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def pricetree(callback: types.CallbackQuery):
    await callback.message.answer(text = f'*📃 Уточните номер пакета:*',reply_markup=keyboard.bots, parse_mode='Markdown')
    await callback.answer()


############################################################################Админское меню#######################################################

@dp.callback_query_handler(text_contains='adminone') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def adminone(call: types.CallbackQuery):
     if call.message.chat.id == config.admin:
        d = sum(1 for line in open('user.txt'))
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f'Вот статистика бота: *{d}* человек', parse_mode='Markdown')
    
        
    


@dp.callback_query_handler(text_contains='admintwo') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def admintwo(callback: types.CallbackQuery):
    await callback.message.answer(f"Команда для рассылки: \n/rassilka текст рассылки")
    await callback.answer()


@dp.callback_query_handler(text_contains='admintree') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def  admintree(callback: types.CallbackQuery):
    await callback.message.answer(f"Проводить рассылки каждый день...")
    await callback.answer()































    ##############################################################
if __name__ == '__main__':
    print('Монстр пчелы запущен!')                                    # ЧТОБЫ БОТ РАБОТАЛ ВСЕГДА с выводом в начале вашего любого текста
executor.start_polling(dp)
##############################################################







