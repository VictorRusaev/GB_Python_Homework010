import requests
import telebot

bot = telebot.TeleBot('YOUR TOKEN')

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    
    try:
        bot.send_message(message.chat.id, res['Valute'][message.text.upper()]['Name'])
        bot.send_message(message.chat.id, res['Valute'][message.text.upper()]['Value'])
        bot.send_message(message.chat.id, res['Valute'][message.text.upper()]['Nominal'])
    except KeyError:
        bot.send_message(message.chat.id, 'Нет такой валюты')

bot.infinity_polling()