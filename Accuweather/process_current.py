import json
from Map_Weather_Icon import map_weather_icon
import re

def process_current():
	with open('raw_current.txt','r') as fh: weather = fh.readlines()
	error = re.search('ServiceUnavailable',weather[0])
	if error:
		message = re.search('Message.*',weather[0]).group()
		with open('current_weather','a') as fh:
			fh.write(message)
		return None
	else:
		icons = map_weather_icon()
		weather = weather[0]
		weather = weather[1:-1]
		weather = json.loads(weather)
		location = weather['Link'].split('/')[5].title()
		observation_time = ' '.join(weather['LocalObservationDateTime'].split('+')[0].split('T'))[5:]
		current_conditions = weather['WeatherText']
		weather_icon = icons[weather['WeatherIcon']]
		day_time = weather['IsDayTime']
		temperature_f = weather['Temperature']['Imperial']['Value']
	

		degree_sign= '\u00b0'
		current = [location +', USA',observation_time, current_conditions, weather_icon, day_time, str(temperature_f)[:-2] + degree_sign]

		with open('current_weather','w') as fh:
			[fh.write(str(item) + '\n') for item in current]


		return None





