#!/usr/bin/python 3
#hi.py

import requests
from bs4 import BeautifulSoup
from process_current import process_current
from process_forecast import process_forecast


#Insert your personal API key here
apikey = # Enter your own Accuweather API key here
#Insert your city code here
city_code = # Enter the Accuweather city code for your city here


#URL for GET request for current weather data from Accuweather for city of choice
url_current = 'http://dataservice.accuweather.com//currentconditions//v1//' + city_code + '?apikey=' + apikey + '&language=en-us&details=true HTTP//1.1'
#URL for GET request for 5 day weather forecast data from Accuweather for city of choice
url_forecast = 'http://dataservice.accuweather.com//forecasts//v1//daily//5day//' + city_code + '?apikey=' + apikey + '&language=en-us&details=false&metric=false HTTP//1.1'

#Perform GET request for current weather data
data_current = requests.get(url_current).text
#Perform GET request for weather forecast data
data_forecast = requests.get(url_forecast).text

#write current weather data to text file
with open('raw_current.txt', 'w') as fh:
	fh.write(data_current)

#write weather forecast to text file
with open('raw_forecast.txt', 'w') as fh:
	fh.write(data_forecast)

#Proccess current weather JSON data
process_current()
#Process weather forecast JSON data
process_forecast()


