import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('19c39945276a7b6c761df14f7d610f97', config_dict)
mgr = owm.weather_manager()
bot = telebot.TeleBot("2011318901:AAHR8DhrBF0gaP9g2yBH9d1xEtop9apwnR8")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    #bot.reply_to(message, message.text)
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    answer = 'В ' + message.text + ' сейчас ' + str(temp) + ' градусов, ' + w.detailed_status + '\n'
    if temp < 10:
        answer += 'На улице холодно, надень шапку'
    elif temp < 20:
        answer += 'На улице прохладно, накинь куртку'
    else:
        answer += 'За окном жаришка, в футболке будет самое то'

    bot.send_message(message.chat.id, answer)


bot.infinity_polling()
