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

import telebot
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()

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
                         "№1 Введите линк на ваш профиль")

        await meinfo.Q1.set()                                    # и начинает ждать наш ответ.

@dp.message_handler(state=meinfo.Q1)                                # Как только бот получит ответ, вот это выполнится
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer1=answer)                            # тут же он записывает наш ответ (наш линк)

    await message.answer("Линк сохранён. \n"
                         "№2 Введите текст.")
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

    await message.answer(f'Ваша ссылка на профиль : {answer1}\nВаш текст:\n{answer2}')    # Ну и выводим линк с текстом который бот записал
 
    await state.finish()




###############################################################################обычные текст#############################################################################




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

    await bot.send_message(message.chat.id, f"ПРИВЕТ, *{message.from_user.first_name},* БОТ РАБОТАЕТ", reply_markup=keyboard.start, parse_mode='Markdown')

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
async def get_message(message):
    if message.text == "Клиенты онлайн📲":
         await bot.send_message(message.chat.id, text= 'Онлайн сейчас📲: ' + str(random.randint(10, 19)))


    if message.text == "Отзывы🕵":
        await bot.send_message(message.chat.id, text = "Просмотр отзывов компании📖", reply_markup=keyboard.stats, parse_mode='Markdown')

    if message.text == "Cвязаться с менеджером для личной консультации📈":
        link1 = open('link.txt', encoding="utf-8") # Вытаскиваем с нашей "БД" инфу, помещаем в переменную и выводим её
        link = link1.read()

        text1 = open('text.txt', encoding="utf-8") # Вытаскиваем с нашей "БД" инфу, помещаем в переменную и выводим её
        text = text1.read()

        await bot.send_message(message.chat.id, text = f"Контент-менеджер👨‍💼: {link}\n{text}")


    if message.text == "Оплата💸":
        await bot.send_message(message.chat.id, text = "Выберите удобный способ💳", reply_markup=keyboard.payment, parse_mode='Markdown')




        ############################################ОТЗЫВЫ############################################################################################################################

        



@dp.callback_query_handler(text_contains='join') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def join(callback: types.CallbackQuery):
    await callback.message.answer('Loading....')
    card_href = 'https://telemetr.me/content/avitov#google_vignette'
    driver.get(card_href)
    sleep(2)
    cards = driver.find_elements_by_div('card-body')
    for i in range(len(cards)):
        bot.send_message(message.chat.id, cards[i].get_attribute('href'))
    






    ############################################ОПЛАТА############################################################################################################################




@dp.callback_query_handler(text_contains='Jove') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "JOIN" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "JOIN"
async def Jove(callback: types.CallbackQuery):
    await callback.message.answer('text 2')
    await callback.answer()
    
       
       
    



@dp.callback_query_handler(text_contains='canceel') # МЫ ПРОПИСЫВАЛИ В КНОПКАХ КАЛЛБЭК "cancle" ЗНАЧИТ И ТУТ МЫ ЛОВИМ "cancle"
async def canceel(callback: types.CallbackQuery):
    await callback.message.answer('text 1')
    await callback.answer()    






















    ##############################################################
if __name__ == '__main__':
    print('Монстр пчелы запущен!')                                    # ЧТОБЫ БОТ РАБОТАЛ ВСЕГДА с выводом в начале вашего любого текста
executor.start_polling(dp)
##############################################################







