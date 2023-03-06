import telebot
from telebot import types

bot = telebot.TeleBot('5895426188:AAGeesw_OVKurBcmJaNv-aUJ46t0vwYhx7M')

@bot.message_handler(commands=['start'])
def day(message):
    markup = types.ReplyKeyboardMarkup(row_width=5)
    pn = types.InlineKeyboardButton('Понедельник',callback_data='pn')
    vt = types.InlineKeyboardButton('Вторник',callback_data='vt')
    sr = types.InlineKeyboardButton('Среда',callback_data='sr')
    cht = types.InlineKeyboardButton('Четверг',callback_data='cht')
    pt = types.InlineKeyboardButton('Пятница',callback_data='pt')
    markup.add(pn,vt,sr,cht,pt)
    bot.send_message(message.chat.id,'День недели:',reply_markup=markup)
@bot.message_handler(func=lambda call:True)
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item8a = types.InlineKeyboardButton('8A',callback_data='8a')
    item8b = types.InlineKeyboardButton('8Б',callback_data='8b')
    item8v = types.InlineKeyboardButton('8В',callback_data='8v')
    item9a = types.InlineKeyboardButton('9А',callback_data='9a')
    item9b = types.InlineKeyboardButton('9Б',callback_data='9b')
    item9v = types.InlineKeyboardButton('9B',callback_data='9v')
    item10a = types.InlineKeyboardButton('10A',callback_data='10a')
    item11a = types.InlineKeyboardButton('11А',callback_data='11a')
    item11b = types.InlineKeyboardButton('11Б',callback_data='11b')
    markup.add(item8a,item8b,item8v,item9a,item9b,item9v,item10a,item11a,item11b)
    bot.send_message(message.chat.id,'Класс:',reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '8a':
            bot.send_message(call.message.chat.id, 'тут расписание 8а')
        elif call.data == '8b':
            bot.send_message(call.message.chat.id, 'тут расписание 8б')
        elif call.data == '8v':
            bot.send_message(call.message.chat.id, 'тут расписание 8в')
        elif call.data == '9a':
            bot.send_message(call.message.chat.id, 'тут расписание 9а')
        elif call.data == '9b':
            bot.send_message(call.message.chat.id, 'тут расписание 9б')
        elif call.data == '9v':
            bot.send_message(call.message.chat.id, 'тут расписание 9в')
        elif call.data == '10a':
            bot.send_message(call.message.chat.id, 'тут расписание 10а')
        elif call.data == '11a':
            bot.send_message(call.message.chat.id, 'тут расписание 11а')
        elif call.data == '11b':
            bot.send_message(call.message.chat.id, 'тут расписание 11б')



bot.polling()    