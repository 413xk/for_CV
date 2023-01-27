from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('19c39945276a7b6c761df14f7d610f97', language = 'ru')
mgr = owm.weather_manager()

place = input('Введите город: ')
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather
print(w)