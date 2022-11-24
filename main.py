import telebot
import config
import random
import requests
from DATE import base

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


def get_weather(city, open_weather_token):
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        print(data)
        city = data['name']
        weather = data['main']['temp']
        return [city, weather]
    except Exception as e:
        print(repr(e))


#print(get_weather('saratov', config.WEATHER_TOKEN))


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "Как дела?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Отлично, как сам?", reply_markup=markup)
        elif message.text == "Температура":
            bot.send_message(message.chat.id, "В каком городе вы живете?")
        else:
            flag=0
            for key in base:
                if (key==message.text):
                    print(message.text)
                    r = get_weather(base[message.text[0].upper() + message.text[1:].lower()].lower(), config.WEATHER_TOKEN)
                    print(r)
                    bot.send_message(message.chat.id, f"В вашем городе {r[1]}")
                    flag=1
                    break
                else:
                    continue
            if (flag==0):
                bot.send_message(message.chat.id, f"Отправляйся в начальную школу, неуч!")

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "Как дела?":

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, "Отлично, как сам?", reply_markup=markup)
        elif message.text == "Температура":
            bot.send_message(message.chat.id, "В каком городе вы живете?")
        else:
            base = {'москва': 'moscow','саратов': 'carotov'}
            print(message.text)
            r = get_weather(base[(message.text.lower())], config.WEATHER_TOKEN)
            print(r)
            bot.send_message(message.chat.id, f"В вашем городе {r[1]}")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, "Вот и отлично")
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, "Это грустно")
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
