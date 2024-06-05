import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def handler_start(message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['button'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Link')
    markup.add(button1)
    bot.send_message(message.chat.id, 'Use for enjoy', reply_markup=markup)


@bot.message_handler()
def sending(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "Hello! Do y wanna know about investment "
                                          "(don't say No)")
    elif message.text == 'Yes':
        bot.send_message(message.chat.id, "Let's start! Write /button")
    elif message.text == 'No':
        bot.send_message(message.chat.id, 'I dont believe y, try again =)')
    elif message.text == '/help':
        bot.send_message(message.chat.id, 'Write: Hello and use Yes or No')
    elif message.text == 'Link':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button2 = types.KeyboardButton("Wrote")
        markup.add(button2)
        bot.send_message(message.chat.id, 'https://www.tinkoff.ru/invest/research/strategy/2024/',
                         reply_markup=markup)
    elif message.text == "Wrote":
        bot.send_message(message.chat.id, 'Thank you for reading!')
    else:
        bot.send_message(message.chat.id, 'Incorrect. Write /help')


bot.polling(non_stop=True)

if __name__ == '__main__':
    bot.polling(none_stop=True)
