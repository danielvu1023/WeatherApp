from flask import Flask, request, jsonify
from openWeatherService import OpenWeatherService

app = Flask(__name__)
weatherService = OpenWeatherService(
"Dd29faab298c99921ec95069c3b99bfe"
)

@app.route("/")
def hello_world():
    return "Hello World"

# Path Param
@app.route("/name/<name>", methods=['GET', 'POST'])
def path_param_test(name):
    return "Hello " + name

# Query Param
@app.route("/query")
def query_param_test():
    print(request.args)
    return "Hello " + request.args.get("person")

# JSON Body POST
@app.route("/body", methods=['POST'])
def body_test():
    print(request.get_json())
    return jsonify(request.get_json())

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

# POST Current and Forecast