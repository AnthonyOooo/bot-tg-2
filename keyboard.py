from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

######################################################
start = types.ReplyKeyboardMarkup(resize_keyboard=True) # СОЗДАЕМ ВООБЩЕ ОСНОВУ ДЛЯ КНОПОК

online = types.KeyboardButton("Клиенты онлайн📲") # готово            # ДОБАВЛЯЕМ КНОПКУ ИНФОРМАЦИИ
peviews = types.KeyboardButton("Отзывы🕵")  # парсинг           # ДОБАВЛЯЕМ КНОПКУ СТАТИСТИКИ
price = types.KeyboardButton("Прайс-лист📃") # текст
payment= types.KeyboardButton("Оплата💸") # текст
razrab = types.KeyboardButton("Cвязаться с менеджером для личной консультации📈") # готово           # ДОБАВЛЯЕМ КНОПКУ РАЗРАБОТЧИК




start.add(peviews, online, price, payment) #ДОБАВЛЯЕМ ИХ В БОТА\
start.add(razrab)


stats = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
stats.add(InlineKeyboardButton(f'стр.1📃', callback_data = 'join')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'стр.2📃', callback_data = 'cancle')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'стр.3📃', callback_data = 'canclee')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'стр.4📃', callback_data = 'cancleee')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'стр.5📃', callback_data = 'cancleeee')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ




payment = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
payment.add(InlineKeyboardButton(f'Qiwi🥝', callback_data = 'Jove')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
payment.add(InlineKeyboardButton(f'Сбербанк🏦', callback_data = 'canceel')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ













