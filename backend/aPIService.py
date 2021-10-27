# API Microservice that will handle sending HTTP requests to any endpoint
import requests
from typing import Optional, TypedDict

class ApiResponse(TypedDict):
    statusCode: str
    message: Optional[str]
    data: Optional[str]

class ApiService: 
    def __init__(self, headers: dict=dict()) -> None:
        self.headers = headers


    def makeGetRequest(self, endpoint: str, queryParams: dict=dict()) -> ApiResponse:
        r = requests.get(endpoint, params=queryParams, headers=self.headers)
        
        response = ApiResponse(
        statusCode=r.status_code, 
        message="Get request to endpoint: " + endpoint + " completed", 
        data=r.json())

        return response
        

    def makePostRequest(self, endpoint: str, payLoad: dict=dict()) -> ApiResponse:
        r = requests.post(endpoint, data=payLoad, headers=self.headers)

        response = ApiResponse(
        statusCode=r.status_code, 
        message="Get request to endpoint: " + endpoint + "completed", 
        data=r.json())
        
        return response

    def makePutRequest(self, endpoint: str, payLoad: dict=dict()) -> ApiResponse:
        r = requests.put(endpoint, data=payLoad, headers=self.headers)

        response = ApiResponse(
        statusCode=r.status_code, 
        message="Get request to endpoint: " + endpoint + "completed", 
        data=r.json())
        
        return response
       

    def makeDeleteRequest(self, endpoint: str, payLoad: dict=dict()) -> ApiResponse:
        r = requests.delete(endpoint, data=payLoad, headers=self.headers)

        response = ApiResponse(
        statusCode=r.status_code, 
        message="Get request to endpoint: " + endpoint + "completed", 
        data=r.json())
        
        return response


