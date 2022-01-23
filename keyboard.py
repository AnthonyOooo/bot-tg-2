from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

######################################################
start = types.ReplyKeyboardMarkup(resize_keyboard=True)
admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
keys = types.ReplyKeyboardMarkup(resize_keyboard=True)
bothelp = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
connect = types.ReplyKeyboardMarkup(resize_keyboard=True)
manager = types.ReplyKeyboardMarkup(resize_keyboard=True)
pack = types.ReplyKeyboardMarkup(resize_keyboard=True)
pay = types.ReplyKeyboardMarkup(resize_keyboard=True)
done = types.ReplyKeyboardMarkup(resize_keyboard=True)




 # СОЗДАЕМ ВООБЩЕ ОСНОВУ ДЛЯ КНОПОК

online = types.KeyboardButton("Ꮶᴧиᴇнᴛы ᴏнᴧᴀйн📲")#+++
payment= types.KeyboardButton("Ꮻᴨᴧᴀᴛᴀ💸") #---          
price = types.KeyboardButton("Пᴩᴀйᴄ-ᴧиᴄᴛ📃")#---
peviews = types.KeyboardButton("Ꮻᴛɜыʙы и Ꮯᴛᴀᴛиᴄᴛиᴋᴀ🕵️") #+++
razrab = types.KeyboardButton("Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ дᴧя ᴧичнᴏй ᴋᴏнᴄуᴧьᴛᴀции📈")
static = types.KeyboardButton("Адʍинᴄᴋиᴇ ᴋᴏнɸиᴦуᴩᴀции👩‍💻")
news = types.KeyboardButton("Измени новости🏪")
newss = types.KeyboardButton("Нᴏʙᴏᴄᴛи🏪") #+++ 
chatonline = types.KeyboardButton("Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲")





start.add(peviews, online, price, payment, newss) #ДОБАВЛЯЕМ ИХ В БОТА\
start.add(razrab)
admin.add(static,news)
keys.add(peviews, online, price, payment, newss)
keys.add(razrab)
menu.add(peviews, online, price, payment, newss)
menu.add(razrab)
connect.add(chatonline)
manager.add(razrab)
pack.add(price)
pay.add(payment)
done.add(peviews)


stats = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
stats.add(InlineKeyboardButton(f'Сᴛᴀᴛиᴄᴛиᴋᴀ ɜᴀᴋᴀɜᴏʙ📊', callback_data = 'join')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Пᴀʍяᴛᴋᴀ ᴀнᴀᴧиɜᴀ ниɯи <Аʙиᴛᴏ>📃', callback_data = 'cancle')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Вᴄᴇᴦᴏ ɜᴀᴋᴀɜᴏʙ🏪', callback_data = 'cancl')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ





payment = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
payment.add(InlineKeyboardButton(f'Ꭷiwi🥝', callback_data = 'Jove')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
payment.add(InlineKeyboardButton(f'Ꮯбᴇᴩбᴀнᴋ🏦', callback_data = 'canceel')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
payment.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ






razrab = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
razrab.add(InlineKeyboardButton(f'Ꮶᴏнᴛᴇнᴛ-ʍᴇнᴇджᴇᴩ👨‍🏫', callback_data = 'content')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
razrab.add(InlineKeyboardButton(f'Зᴀᴨᴩᴏᴄ ᴀудиᴛᴀ(бᴇᴄᴨᴧᴀᴛнᴏ)📈', callback_data = 'audit')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
razrab.add(InlineKeyboardButton(f'Ꭲᴇх.Пᴏддᴇᴩжᴋᴀ👩‍💻', callback_data = 'podder')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
razrab.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
 






price = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
price.add(InlineKeyboardButton(f'Базовый план📑', callback_data = 'priceone')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
price.add(InlineKeyboardButton(f'План "Премиум"📔', callback_data = 'pricetwo')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
price.add(InlineKeyboardButton(f'Бизнес-план📚', callback_data = 'pricetree')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
price.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ





############################################################################Админское меню#######################################################




static = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
static.add(InlineKeyboardButton(f'Статистика бота📑', callback_data = 'adminone')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
static.add(InlineKeyboardButton(f'Рассылка📔', callback_data = 'admintwo')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
static.add(InlineKeyboardButton(f'Другое📚', callback_data = 'admintree')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
static.add(InlineKeyboardButton(f'Назад🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ





############################################################################ЧАТТТ ОНЛАЙН#######################################################























