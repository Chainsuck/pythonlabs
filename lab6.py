import telebot
import requests

bot = telebot.TeleBot('5838871759:AAFqscCpiEmcDdEMOxrQ-8Ek89JiR84mOIM')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, чтобы узнать, что может этот бот, напиши /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'этот бот присылает тебе фото, какое - неизвестно. чтобы попробовать, напиши /pic')

@bot.message_handler(commands=['pic'])
def fox(message):
    r = requests.get('https://random.imagecdn.app/800/900')
    q = r.url
    bot.send_photo(message.chat.id, q)


bot.polling(none_stop=True)