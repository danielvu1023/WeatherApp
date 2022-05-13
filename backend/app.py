from flask import Flask, request, jsonify
from openWeatherService import OpenWeatherService
from flask_cors import CORS

app = Flask(__name__)
weatherService = OpenWeatherService(
"Dd29faab298c99921ec95069c3b99bfe"
)
# Cors lets programs not in the same domain call our API 
CORS(app)

# Get Current Weather
@app.route("/weather/current/<cityName>", methods=['GET'])
def getCurrentWeatherOfCity(cityName):
    weatherDataResponse = weatherService.getCurrentWeather(cityName)
    if(weatherDataResponse.get("statusCode") == 200):
        response  = {
            "statusCode": 200,
            "weatherData": {
                "cityName": cityName,
                "temperature": weatherDataResponse.get("data").get("main").get("temp")
            }
        }
    else:
        response  = weatherDataResponse

    return jsonify(response)

# Get Forecast Weather
@app.route("/weather/forecast", methods=['GET'])
def getForecastWeatherOfCity():
    cityName = request.args.get("q")
    weatherDataResponse = weatherService.getForecast(cityName)
    
    if(weatherDataResponse.get("statusCode") == 200):
        weatherDataList = []
        for date in weatherDataResponse.get("data").get("list"):
            currentDate = date.get("dt_txt")
            currentTemp = date.get("main").get("temp")
            weatherDataList.append({
                "currentTime": currentDate, 
                "temperature": currentTemp
                })
        freqCounter = {}
        tempTracker = {} 
        previous = ""  
        for weather in weatherDataList:
            if weather["currentTime"][9] not in freqCounter:
                if previous != "":
                    prevFreq = str(int(weather["currentTime"][9]) - 1)
                    tempTracker[previous] /= freqCounter[prevFreq] 
                    tempTracker[previous] = round(tempTracker[previous], 2)
                freqCounter[weather["currentTime"][9]] = 1
                tempTracker[weather["currentTime"][0:10]] = weather["temperature"]
                previous = weather["currentTime"][0:10]
            elif weatherDataList.index(weather) == len(weatherDataList) - 1:
                tempTracker[weather["currentTime"][0:10]] /= freqCounter[weather["currentTime"][9]]
                tempTracker[weather["currentTime"][0:10]] = round(tempTracker[weather["currentTime"][0:10]], 2)
            else:
                freqCounter[weather["currentTime"][9]] += 1
                tempTracker[weather["currentTime"][0:10]] += weather["temperature"]     
        response  = {
            "statusCode": 200,
            "weatherData": {
                "cityName": cityName,
                "forecastList": tempTracker
            }
        }
    else:
        response  = weatherDataResponse

    return jsonify(response)


if __name__ == '__main__':
    app.run()

