import telebot
import config
import random
import requests

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
            base = {'Абакан':'Abakan','Альметьевск':'Almetyevsk','Анадырь':'Anadyr','Анапа':'Anapa',
                    'Архангельск':'Arkhangelsk','Астрахань':'Astrakhan','Барнаул':'Barnaul',
                    'Белгород':'Belgorod','Беслан':'Beslan','Бийск':'Biysk','Биробиджан' :'Birobidzhan',
                    'Благовещенск':'Blagoveshchensk', 'Бологое' :'Bologoye','Брянск':'Bryansk',
                    'Великий Новгород':'Veliky Novgorod','Великий Устюг':'Veliky Ustyug',
                    'Владивосток':'Vladivostok','Владикавказ':'Vladikavkaz','Владимир':'Vladimir',
                    'Волгоград':'Volgograd','Вологда':'Vologda','Воркута':'Vorkuta','Воронеж':'Voronezh',
                    'Гатчина':'Gatchina','Гдов':'Gdov','Геленджик':'Gelendzhik','Горно-Алтайск':'Gorno-Altaysk',
                    'Грозный':'Grozny','Гудермес':'Gudermes','Гусь-Хрустальный':'Gus-Khrustalny',
                    'Дзержинск':'Dzerzhinsk','Дмитров':'Dmitrov','Дубна':'Dubna',
                    'Ейск':'Yeysk','Екатеринбург':'Yekaterinburg','Елабуга':'Yelabuga','Елец':'Yelets',
                    'Ессентуки':'Yessentuki','Златоуст':'Zlatoust','Иваново':'Ivanovo',
                    'Ижевск':'Izhevsk', 'Иркутск':'Irkutsk','Йошкар-Ола':'Yoshkar-Ola','Казань':'Kazan',
                    'Калининград':'Kaliningrad','Калуга':'Kaluga','Кемерово':'Kemerovo','Кисловодск':'Kislovodsk',
                    'Комсомольск-на-Амуре':'Komsomolsk-on-Amur','Котлас':'Kotlas','Краснодар':'Krasnodar',
                    'Красноярск':'Krasnoyarsk','Курган':'Kurgan','Курск':'Kursk','Кызыл':'Kyzyl',
                    'Лениногорск':'Leninogorsk','Ленск':'Lensk','Липецк':'Lipetsk','Луга':'Luga','Любань':'Lyuban',
                    'Люберцы':'Lyubertsy','Магадан':'Magadan','Майкоп':'Maykop','Махачкала':'Makhachkala',
                    'Миасс':'Miass','Минеральные Воды':'Mineralnye Vody','Мирный':'Mirny','Москва':'Moscow',
                    'Мурманск':'Murmansk','Муром':'Murom','Мытищи':'Mytishchi','Набережные Челны':'Naberezhnye Chelny',
                    'Надым':'Nadym','Нальчик':'Nalchik','Назрань':'Nazran','Нарьян-Мар':'Naryan-Mar',
                    'Находка':'Nakhodka','Нижневартовск':'Nizhnevartovsk','Нижнекамск':'Nizhnekamsk',
                    'Нижний Новгород':'Nizhny Novgorod','Нижний Тагил':'Nizhny Tagil','Новокузнецк':'Novokuznetsk',
                    'Новосибирск':'Novosibirsk','Новый Уренгой':'Novy Urengoy','Норильск':'Norilsk',
                    'Обнинск':'Obninsk','Октябрьский':'Oktyabrsky','Омск':'Omsk','Оренбург':'Orenburg',
                    'Орехово-Зуево':'Orekhovo-Zuyevo','Орёл':'Oryol','Пенза':'Penza','Пермь':'Perm',
                    'Петрозаводск':'Petrozavodsk','Петропавловск-Камчатский':'Petropavlovsk-Kamchatsky',
                    'Подольск':'Podolsk','Псков':'Pskov','Пятигорск':'Pyatigorsk',
                    'Ростов-на-Дону':'Rostov-on-Don', 'Рыбинск':'Rybinsk','Рязань':'Ryazan','Салехард':'Salekhard',
                    'Самара':'Samara','Санкт-Петербург':'Saint-Petersburg','Саранск':'Saransk','Саратов':'Saratov',
                    'Северодвинск':'Severodvinsk','Смоленск':'Smolensk','Соль-Илецк':'Sol-Iletsk','Сочи':'Sochi',
                    'Ставрополь':'Stavropol','Сургут':'Surgut','Сыктывкар':'Syktyvkar',
                    'Тамбов':'Tambov','Тверь':'Tver','Тобольск':'Tobolsk','Тольятти':'Tolyatti','Томск':'Tomsk',
                    'Туапсе':'Tuapse','Тула':'Tula','Тында':'Tynda','Тюмень':'Tyumen','Улан-Уде':'Ulan-Ude',
                    'Ульяновск':'Ulyanovsk', 'Уфа':'Ufa','Хабаровск':'Khabarovsk','Ханты-Мансийск':'Khanty-Mansiysk',
                    'Чебаркуль':'Chebarkul','Чебоксары':'Cheboksary','Челябинск':'Chelyabinsk','Череповец':'Cherepovets',
                    'Черкесск':'Cherkessk','Чистополь':'Chistopol', 'Чита':'Chita','Шадринск':'Shadrinsk',
                    'Шатура':'Shatura','Шуя':'Shuya','Элиста':'Elista','Энгельс':'Engels',
                    'Южно-Сахалинск':'Yuzhno-Sakhalinsk','Якутск':'Yakutsk','Ярославль':'Yaroslavl'}
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
