import os
from dotenv import load_dotenv

# Import open weather api key from .env file
load_dotenv()

OPENW_API_KEY = os.getenv("OPENW_API_KEY")

import requests

def to_celcius(kelvin:float, round_digit=2) -> float:       
    return round(kelvin-273.15, round_digit)

class OpenWeather:
    def __init__(self, name):
        API_LINK = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={OPENW_API_KEY}"
        self.response = requests.get(API_LINK).json()

    def name(self) -> str:
        return self.response["name"]

    def coord(self) -> dict:
        return self.response["coord"]

    def weather(self) -> dict: 
        temp:dict = self.response["weather"][0]
        main = temp["main"]
        description = temp["description"]

        return {"main":main, "description":description}

    def main(self) -> dict:
        return self.response["main"]

    def temperature(self, round_digit=2) -> float:
        return self.main()["temp"]

    def feels_like(self, round_digit=2) -> float:
        return self.main()["feels_like"]

    def temp_min(self, round_digit=2) -> float:
        return self.main()["temp_min"]

    def temp_max(self, round_digit=2) -> float:
        return self.main()["temp_max"]

    def pressure(self) -> float:
        return self.main()["pressure"]

    def humidity(self) -> float:
        return self.main()["humidity"]
    
    def wind(self) -> dict:        
        return self.response["wind"]

    def visibility(self) -> float:
        return self.response["visibility"]

    def clouds(self) -> dict:
        return self.response["clouds"]
    
    def sunrise(self) -> dict:
        return self.response["sys"]["sunrise"]
    
    def sunset(self) -> dict:
        return self.response["sys"]["sunset"]

    def cod(self) -> int:
        return self.response["cod"]
    
    def timezone(self) -> dict: 
        return self.response["timezone"]

    def country(self) -> dict:
        return self.response["sys"]["country"]

    def icon_url(self) -> str:
        temp:dict = self.response["weather"][0]
        return f"https://openweathermap.org/img/w/{temp['icon']}"


kolkata = OpenWeather("Paris")

print(
    kolkata.name(),
    kolkata.coord(),
    kolkata.weather(),
    kolkata.main(),
    kolkata.temperature(),
    kolkata.feels_like(),
    kolkata.temp_min(),
    kolkata.temp_max(),
    kolkata.pressure(),
    kolkata.humidity(),
    kolkata.wind(),
    kolkata.visibility(),
    kolkata.clouds(),
    kolkata.sunrise(),
    kolkata.sunset(),
    kolkata.cod(),
    kolkata.timezone(),
    kolkata.country(),
    kolkata.icon_url()
)


