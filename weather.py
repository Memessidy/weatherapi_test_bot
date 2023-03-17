import urllib.request
import json
import datetime
from string_convertor.ua_to_lat import get_string
from tokens import openweather_token


def get_weather_data(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "q=" + city + "&appid=" + openweather_token + "&units=metric"
    response = None
    try:
        response = urllib.request.urlopen(url)
    except Exception as exc:
        print(exc)
        print("Перевірте назву міста")

    if response.status == 200:
        data = response.read().decode('utf-8')
        return json.loads(data)
    return None


codes = {
    "Clear": "Ясно \U00002600",
    "Clouds": "Хмарно  \U00002601",
    "Rain": "Дощ \U00002614",
    "Drizzle": "Дощ \U00002614",
    "Thunderstorm": "Гроза \U000026A1",
    "Snow": "Сніг \U0001F328",
    "Mist": "Туман \U0001F32B"
}


def parse_response(weather_data):
    city = weather_data['name']
    cur_weather = weather_data['main']['temp']

    weather_description = weather_data['weather'][0]['main']
    if weather_description in codes:
        symbol = codes[weather_description]
    else:
        symbol = "*Погода*"

    humidity = weather_data['main']['humidity']
    pressure = weather_data['main']['pressure']
    wind_speed = weather_data['wind']['speed']
    sunrise_timestamp = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset_timestamp = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
    length_of_the_day = sunset_timestamp - sunrise_timestamp
    smile = "\U0001F603"

    return f"""
    Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} {smile}
    Погода в місті: {city}
    Температура: {cur_weather}°C {symbol}
    Вологість: {humidity}%
    Тиск: {pressure} мм.рт.ст.
    Швидкість вітру: {wind_speed}м/с
    Схід сонця: {sunrise_timestamp.strftime('%H:%M:%S')}
    Захід сонця: {sunset_timestamp.strftime('%H:%M:%S')}
    Тривалість дня: {length_of_the_day}
    ************
    """


def get_weather(city_name):
    city_name = get_string(city_name)
    weather_data = get_weather_data(city_name)
    return parse_response(weather_data)
