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
ref = types.ReplyKeyboardMarkup(resize_keyboard=True)
other = types.ReplyKeyboardMarkup(resize_keyboard=True)
pakets = types.ReplyKeyboardMarkup(resize_keyboard=True)
prt = types.ReplyKeyboardMarkup(resize_keyboard=True)
bots = types.ReplyKeyboardMarkup(resize_keyboard=True)



 # СОЗДАЕМ ВООБЩЕ ОСНОВУ ДЛЯ КНОПОК

online = types.KeyboardButton("Ꮶᴧиᴇнᴛы ᴏнᴧᴀйн📲")#+++
payment= types.KeyboardButton("Ꮻᴨᴧᴀᴛᴀ💸") #---          
price = types.KeyboardButton("Пᴩᴀйᴄ-ᴧиᴄᴛ📃")#---
peviews = types.KeyboardButton("Ꮻᴛɜыʙы и Ꮯᴛᴀᴛиᴄᴛиᴋᴀ🕵️") #+++
razrab = types.KeyboardButton("Ꮯʙяɜᴀᴛьᴄя ᴄ ʍᴇнᴇджᴇᴩᴏʍ📈")
proch = types.KeyboardButton("Дᴩуᴦᴏᴇ📚")
static = types.KeyboardButton("Адʍинᴄᴋиᴇ ᴋᴏнɸиᴦуᴩᴀции👩‍💻")
news = types.KeyboardButton("Измени новости🏪")
newss = types.KeyboardButton("Ꮋᴏʙᴏᴄᴛи🏪") #+++ 
chatonline = types.KeyboardButton("Ꭹᴄᴛᴀнᴏʙиᴛь ᴄᴏᴇдинᴇниᴇ📲")
dryg = types.KeyboardButton("Пᴏᴧучиᴛь ᴄᴄыᴧᴋу💵")
vash = types.KeyboardButton("Пᴏᴄʍᴏᴛᴩᴇᴛь ᴩᴇɸᴇᴩᴀᴧᴏʙ🙋‍")
ask = types.KeyboardButton("Назад🔹")
one = types.KeyboardButton("Пакет 1 🛍")
two = types.KeyboardButton("Пакет 2 🛍")
tree = types.KeyboardButton("Пакет 3 🛍")
fo = types.KeyboardButton("Пакет 4 🛍")
five = types.KeyboardButton("Пакет 5 🛍")
six =  types.KeyboardButton("Пакет 6 🛍")
pars = types.KeyboardButton("Все пакеты 🛍")
bot = types.KeyboardButton("Зᴀбᴇᴩи ᴄʙᴏᴇᴦᴏ бᴏᴛᴀ🤖")
bibo = types.KeyboardButton("Зᴀᴋᴀɜᴀᴛь бᴏᴛᴀ дᴧя биɜнᴇᴄᴀ 🏭")








start.add(peviews, online, price, payment, newss) #ДОБАВЛЯЕМ ИХ В БОТА
start.add(razrab, proch)
admin.add(static,news)
admin.add(ask)
keys.add(peviews, online, price, payment, newss)
keys.add(razrab, proch)
menu.add(peviews, online, price, payment, newss)
menu.add(razrab, proch)
connect.add(chatonline)
connect.add(ask)
manager.add(razrab)
manager.add(ask)
pack.add(price)
pack.add(ask)
pay.add(payment)
pay.add(ask)
done.add(peviews)
done.add(ask)
ref.add(dryg, vash)
ref.add(ask)
other.add(chatonline)
other.add(dryg, vash)
other.add(ask)
pakets.add(one, two, tree)
pakets.add(fo, five, six)
pakets.add(ask)
prt.add(pars)
prt.add(ask)
bots.add(bot)
bots.add(bibo)
bots.add(ask)



stats = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
stats.add(InlineKeyboardButton(f'Сᴛᴀᴛиᴄᴛиᴋᴀ ɜᴀᴋᴀɜᴏʙ📊', callback_data = 'join')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Пᴀʍяᴛᴋᴀ ᴀнᴀᴧиɜᴀ ниɯи <Аʙиᴛᴏ>📃', callback_data = 'cancle')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Вᴄᴇᴦᴏ ɜᴀᴋᴀɜᴏʙ🏪', callback_data = 'cancl')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ





payment = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
payment.add(InlineKeyboardButton(f'Аʙиᴛᴏ 🛒', callback_data = 'Jove')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
payment.add(InlineKeyboardButton(f'Пᴀᴩᴄинᴦ 📄', callback_data = 'vroom')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
payment.add(InlineKeyboardButton(f'Телеграм боты 🤖', callback_data = 'hou')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
payment.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ






razrab = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
razrab.add(InlineKeyboardButton(f'Ꮶᴏнᴛᴇнᴛ-ʍᴇнᴇджᴇᴩ👨‍🏫', callback_data = 'content')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
razrab.add(InlineKeyboardButton(f'Зᴀᴨᴩᴏᴄ ᴀудиᴛᴀ(бᴇᴄᴨᴧᴀᴛнᴏ)📈', callback_data = 'audit')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
razrab.add(InlineKeyboardButton(f'Ꭲᴇх.Пᴏддᴇᴩжᴋᴀ👩‍💻', callback_data = 'podder')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
razrab.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
 






price = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
price.add(InlineKeyboardButton(f'Авито продвижение📑', callback_data = 'priceone')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
price.add(InlineKeyboardButton(f'Парсинг услуги📔', callback_data = 'pricetwo')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
price.add(InlineKeyboardButton(f'Телеграм бот для вашего бизнеса📚', callback_data = 'pricetree')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
price.add(InlineKeyboardButton(f'Назад 🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ





############################################################################Админское меню#######################################################




static = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
static.add(InlineKeyboardButton(f'Статистика бота📑', callback_data = 'adminone')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
static.add(InlineKeyboardButton(f'Рассылка📔', callback_data = 'admintwo')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
static.add(InlineKeyboardButton(f'Другое📚', callback_data = 'admintree')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
static.add(InlineKeyboardButton(f'Назад🔙', callback_data = 'canc')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ







############################################################################ЧАТТТ ОНЛАЙН#######################################################





######################################################################ДРУГОЕ####################################################################


















