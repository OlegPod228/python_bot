import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)
emoji = ''
text = ''
messages = ''

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Напиши /g чтобы сгенерировать текст из выбраных смайликов😜')
    elif message.text == '/g':
        bot.send_message(message.chat.id, ' Введите смайлик✍🏼:')
        bot.register_next_step_handler(message, smile)
    else:
        bot.send_message(message.chat.id, 'Даже не знаю что ответить...🙄 \nНапиши /g 😉')

def smile(message):
    global emoji
    if message != bot.message_handler(content_types=["sticker"]):
        emoji = message.text
        bot.send_message(message.chat.id, 'Введите текст для обработки✍🏼:',)
        bot.register_next_step_handler(message, set_text)

    else:
        bot.send_message(message.chat.id, 'Некорректный смайлик...')
        bot.send_message(message.chat.id, 'Введите смайлик✍🏼:')
        bot.register_next_step_handler(message, smile)

def set_text(message):
    global text
    global messages
    text = message.text
    messages = config.generate(emoji,text)

    #Keyboard
    markup = types.InlineKeyboardMarkup()
    cp = types.InlineKeyboardButton('Переслать',switch_inline_query='\n\n' +messages )
    markup.add(cp)

    try:
        bot.send_message(message.chat.id, messages, reply_markup=markup)
    except:
        bot.send_message(message.chat.id, 'Некорректно введен текст ')
        bot.send_message(message.chat.id, 'Введите текст для обработки✍🏼:')
        bot.register_next_step_handler(message, set_text)

bot.polling(none_stop= True)

