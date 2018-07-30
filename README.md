# Accuweather and Word of the Day Conky Config
![Screenshot](https://github.com/Mooseburger1/Weather_Conky_Config/blob/master/Images/Screenshot%20.png)


[Introduction](intro)

[Requirements](hreq)

[Accuweather API](api)

[Setup](setup)

# <a name = 'intro'>Introduction</a>
--------------------------------------
This is a conky config I created that is simple, not overbearing and useful. It requires Python 3, and an Accuweather API. There are free and paid for API keys. I used the free API which limits you to 50 weather queries a day. This is more than enough for simple weather updates. The API does provide even more in depth weather details, but I focused on keeping this config as simple as needed

# <a name = 'hreq'>Requirements</a>
-----------------------------------------
* Python 3
* BeautifulSoup Python Library
* Json Python Library
* Requests Python Library
* Dancing Script Font (.ttf)
* Accuweather API key

# <a name = 'api'>Accuweather API</a>
--------------------------------------------
You can obtain your own API key by going to https://developer.accuweather.com/ and registering in the upper right hand corner. Again I stuck with the free API key, but you can get the paid for api if you so choose. Once you've obtained your API key, copy it and navigate to the accuweather.py script file in the Accuweather folder. Open it with any editing program, and where it says *"Enter your own Accuweather API key here"* paste your API key there. After you have pasted your API key, you need to insert you city code in the line underneathe that line where it says *"Enter the Accuweather city code for your city here"*. The easiest way to get this city code is to go to the main accuweather website and do a weather search for your city. Once the weather forecast has loaded for your city, look in the URL link. At the end of the URL with be a number - this number is your city code. Copy this code and past it in the appropriate spot in the accuweather.py script file. For example, when I search for weather in austin, the URL returns:
> https://www.accuweather.com/en/us/austin-tx/78701/weather-forecast/351193

So I would paste 351193 into the script file

# <a name = 'setup'>Setup</a>
----------------------------------
Clone or download this whole repository. Place the entire folder in your home directory and rename it **Scripts**. If you do not rename this folder, the paths in the .conkyrc won't be able to find the scripts to run. After you have renamed the folder, go into it and copy the **.conkyrc** file and paste it by itself in your home directory. Next, navigate to ~/Scripts/Accuweather and open a terminal here by right clicking and hitting "open in terminal". Once you have a terminal session open, type:
> \$python3 accuweather.py

This will use your api key and query accuweather for the weather forecast info for your city and overwrite the text files in the original repo with your cities forecast. Next, you need to update your font scripts with the ones used in the conky config. If one doesn't already exist in your home folder, create a new folder and name it **.fonts**. Be sure to put the period in front of fonts. Next, google search "dancing script font .ttf. Download any .ttf file you come across. There's many font sources for linux. If you already have a favorite source for fonts, then use that. Move this .ttf file to the .fonts directory. You might have to log off and log on again for it to take affect. After you've completed all these steps, then that should be it. Open up a terminal session and just type conky. Conky should read the .conkyrc file and render the output. You may need to adjust the conky window size in the settings to fit your screen. I formatted this config to fit my 4k screen. Your results may vary.



