# This service will call Open Weather's API so we can get weather data
from aPIService import ApiService
class OpenWeatherService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_service = ApiService()

    def getCurrentWeather(self, city_name: str):
        endpoint = "https://api.openweathermap.org/data/2.5/weather"
        queryParams = {"q": city_name, "appid": self.api_key, "units": "imperial"}
        response = self.api_service.makeGetRequest(endpoint, queryParams)

        return response

    def getForecast(self, city_name: str):
        endpoint = "https://api.openweathermap.org/data/2.5/forecast"
        queryParams = {"q": city_name, "appid": self.api_key, "units": "imperial"}
        response = self.api_service.makeGetRequest(endpoint, queryParams)

        return response
        

