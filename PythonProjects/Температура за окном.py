from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('19c39945276a7b6c761df14f7d610f97', config_dict)
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
place = input('Put your city here: ')
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')['temp']

print(f'В {place} сейчас', temp, 'градусов,', w.detailed_status )

if temp < 10:
    print('На улице холодно, надень шапку')
elif temp < 20:
    print('На улице норм, но куртку накинь')
else:
    print('За окном жаришка, в футболке будет самое то')