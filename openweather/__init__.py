import os
from dotenv import load_dotenv

# Import open weather api key from .env file
load_dotenv()

OPENW_API_KEY = os.getenv("OPENW_API_KEY")

import requests

def to_celcius(kelvin:float, round_digit=2) -> float:    
    #defining to_celcius   
    return round(kelvin-273.15, round_digit)

class OpenWeather:
    def __init__(self, name):
        API_LINK = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={OPENW_API_KEY}"
        self.response = requests.get(API_LINK).json()

    def name(self) -> str:
        #returning name of city
        return self.response["name"]

    def coord(self) -> dict:
        #coordinates of city
        return self.response["coord"]

    def weather(self) -> dict:
        #returning the weather 
        temp:dict = self.response["weather"][0]
        main = temp["main"]
        description = temp["description"]

        return {"main":main, "description":description}

    def main(self) -> dict:
        return self.response["main"]

    def temperature(self, round_digit=2) -> float:
        #returning the temperature
        return self.main()["temp"]

    def feels_like(self, round_digit=2) -> float:
        #returning what the temperature feels like
        return self.main()["feels_like"]

    def temp_min(self, round_digit=2) -> float:
        #returning the minimum temperature
        return self.main()["temp_min"]

    def temp_max(self, round_digit=2) -> float:
        #returning the maximum temperature
        return self.main()["temp_max"]

    def pressure(self) -> float:
        #returning the atmospheric pressure
        return self.main()["pressure"]

    def humidity(self) -> float:
        #returning the humidity in the city
        return self.main()["humidity"]
    
    def wind(self) -> dict:
        #returning the wind speed        
        return self.response["wind"]

    def visibility(self) -> float:
        #returning air visibility
        return self.response["visibility"]

    def clouds(self) -> dict:
        return self.response["clouds"]
    
    def sunrise(self) -> dict:
        #returning sunrise time
        return self.response["sys"]["sunrise"]
    
    def sunset(self) -> dict:
        #returning sunset time
        return self.response["sys"]["sunset"]

    def cod(self) -> int:
        return self.response["cod"]
    
    def timezone(self) -> dict:
        #returning timezone of the chosen city 
        return self.response["timezone"]

    def country(self) -> dict:
        #returning the country the city is in
        return self.response["sys"]["country"]

    def icon_url(self) -> str:
        #returning icon of weather
        temp:dict = self.response["weather"][0]
        return f"https://openweathermap.org/img/w/{temp['icon']}"