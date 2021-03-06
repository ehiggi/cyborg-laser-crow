# weather.py
# Nick Florentius - 2/2/2019
# Fetches weather data using OpenWeatherMap APIs
# Maybe parses too
# API Key:  1bb1edd4423c322cbe59b8b6a425f382
# Useful documentation:  https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/


import requests

api_key = "1bb1edd4423c322cbe59b8b6a425f382"

w=[]

def initW():  # initialize weather dict
    global w
    w = [{'low': 999, 'high': -999, 'date': '', 'weather': '', 'rain': 0, 'snow': 0}]

def hasSnow(x, i):
    try:
        isEmpty = (x["list"][i]['snow'] != {})
        return isEmpty
    except KeyError:
        return False


def hasRain(x, i):
    try:
        isEmpty = (x["list"][i]['rain'] != {})
        return isEmpty
    except KeyError:
        return False


def getWeather(z):  # download/update weather, pass in zip code
    initW()
    z = str(z)  # ensure zip is string
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + api_key + "&zip=" + z + ",us"

    response = requests.get(complete_url)
    x = response.json()
    # Weather data is given in 3 hour increments over 5 days, finds peak high and low temps for each of 5 days
    count = x["cnt"]  # number of data points

    curDay = 0
    curDate = x["list"][0]['dt_txt'][0:10]  # 0-10 is the date portion of the date&time attribute
    for i in range(count):
        date = x["list"][i]['dt_txt'][0:10]
        if date != curDate:  # if current weather data date is not the current one update what we are now on
            curDay += 1
            curDate = date
            w.append({'low': 999, 'high': -999, 'date': '', 'weather': '', 'rain': 0, 'snow': 0})
        w[curDay]['date'] = curDate
        w[curDay]['high'] = max((x["list"][i]['main']['temp_max']), w[curDay]['high'])
        w[curDay]['low'] = min((x["list"][i]['main']['temp_min']), w[curDay]['low'])
        w[curDay]['weather'] = x["list"][i]['weather'][0]['main']
        if hasRain(x, i):
            w[curDay]['rain'] += x["list"][i]['rain']['3h']
        if hasSnow(x, i):
            w[curDay]['snow'] += x["list"][i]['snow']['3h']

    for el in w:  # convert temps from kelvin to celsius
        el['low'] -= 273
        el['high'] -= 273
        el['low'] = int(el['low'])
        el['high'] = int(el['high'])

    return w


def printWeather():  # print weather (debug purposes)
    for el in w:
        print("On date: " + str(el['date']) + " lo=" + str(el['low']) + " hi=" + str(el['high']) + " weather=" + el[
            'weather'] + " mm-rain=" + str(el['rain']) + " mm-snow=" + str(el['snow']))


# api.openweathermap.org/data/2.5/forecast?zip=94040,us
