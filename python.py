#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def get_local_weather():
    url = 'https://www.example.com/local-weather'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    weather_info = soup.find('div', class_='weather-info').text
    return weather_info

if __name__ == "__main__":
    weather = get_local_weather()
    print(f"Local Weather Information: {weather}")

