import json
from Map_Weather_Icon import map_weather_icon



def process_forecast():
	with open('raw_forecast.txt') as fh: forecast = fh.readlines()
	
	icons = map_weather_icon()
	
	forecast = json.loads(forecast[0])
	
	#Day 1
	day1_date = '/'.join(forecast['DailyForecasts'][0]['Date'].split('T')[0].split('-')[1:])
	day1_min = forecast['DailyForecasts'][0]['Temperature']['Minimum']['Value']
	day1_max = forecast['DailyForecasts'][0]['Temperature']['Maximum']['Value']
	day1_day_cond = forecast['DailyForecasts'][0]['Day']['IconPhrase']
	day1_day_icon = icons[forecast['DailyForecasts'][0]['Day']['Icon']]
	day1_night_cond = forecast['DailyForecasts'][0]['Night']['IconPhrase']
	day1_night_icon = icons[forecast['DailyForecasts'][0]['Night']['Icon']]

	#Day 2
	day2_date = '/'.join(forecast['DailyForecasts'][1]['Date'].split('T')[0].split('-')[1:])
	day2_min = forecast['DailyForecasts'][1]['Temperature']['Minimum']['Value']
	day2_max = forecast['DailyForecasts'][1]['Temperature']['Maximum']['Value']
	day2_day_cond = forecast['DailyForecasts'][1]['Day']['IconPhrase']
	day2_day_icon = icons[forecast['DailyForecasts'][1]['Day']['Icon']]
	day2_night_cond = forecast['DailyForecasts'][1]['Night']['IconPhrase']
	day2_night_icon = icons[forecast['DailyForecasts'][1]['Night']['Icon']]

	#Day 3
	day3_date = '/'.join(forecast['DailyForecasts'][2]['Date'].split('T')[0].split('-')[1:])
	day3_min = forecast['DailyForecasts'][2]['Temperature']['Minimum']['Value']
	day3_max = forecast['DailyForecasts'][2]['Temperature']['Maximum']['Value']
	day3_day_cond = forecast['DailyForecasts'][2]['Day']['IconPhrase']
	day3_day_icon = icons[forecast['DailyForecasts'][2]['Day']['Icon']]
	day3_night_cond = forecast['DailyForecasts'][2]['Night']['IconPhrase']
	day3_night_icon = icons[forecast['DailyForecasts'][2]['Night']['Icon']]

	#Day 4
	day4_date = '/'.join(forecast['DailyForecasts'][3]['Date'].split('T')[0].split('-')[1:])
	day4_min = forecast['DailyForecasts'][3]['Temperature']['Minimum']['Value']
	day4_max = forecast['DailyForecasts'][3]['Temperature']['Maximum']['Value']
	day4_day_cond = forecast['DailyForecasts'][3]['Day']['IconPhrase']
	day4_day_icon = icons[forecast['DailyForecasts'][3]['Day']['Icon']]
	day4_night_cond = forecast['DailyForecasts'][3]['Night']['IconPhrase']
	day4_night_icon = icons[forecast['DailyForecasts'][3]['Night']['Icon']]

	#Day 5
	day5_date = '/'.join(forecast['DailyForecasts'][4]['Date'].split('T')[0].split('-')[1:])
	day5_min = forecast['DailyForecasts'][4]['Temperature']['Minimum']['Value']
	day5_max = forecast['DailyForecasts'][4]['Temperature']['Maximum']['Value']
	day5_day_cond = forecast['DailyForecasts'][4]['Day']['IconPhrase']
	day5_day_icon = icons[forecast['DailyForecasts'][4]['Day']['Icon']]
	day5_night_cond = forecast['DailyForecasts'][4]['Night']['IconPhrase']
	day5_night_icon = icons[forecast['DailyForecasts'][4]['Night']['Icon']]

	degree_sign= '\u00b0'

	forecast = {'day1': [day1_date, str(day1_min)[:-2]+degree_sign, str(day1_max)[:-2]+degree_sign, day1_day_cond, day1_day_icon, day1_night_cond, day1_night_icon],
				'day2': [day2_date, str(day2_min)[:-2]+degree_sign, str(day2_max)[:-2]+degree_sign, day2_day_cond, day2_day_icon, day2_night_cond, day2_night_icon],
				'day3': [day3_date, str(day3_min)[:-2]+degree_sign, str(day3_max)[:-2]+degree_sign, day3_day_cond, day3_day_icon, day3_night_cond, day3_night_icon],
				'day4': [day4_date, str(day4_min)[:-2]+degree_sign, str(day4_max)[:-2]+degree_sign, day4_day_cond, day4_day_icon, day4_night_cond, day4_night_icon],
				'day5': [day5_date, str(day5_min)[:-2]+degree_sign, str(day5_max)[:-2]+degree_sign, day5_day_cond, day5_day_icon, day5_night_cond, day5_night_icon]}



	with open('weather_forecast.txt', 'w') as fh:
		for key in forecast.keys():
			fh.write('##### ' + str(key) + ' #####' + '\n')
			data = forecast[key]
			[fh.write(str(item) + '\n') for item in data]
			fh.write('\n')

	return None



