
"""
import requests
rsp = requests.get("https://holidays.abstractapi.com/v1/?api_key=344a61a75b3541b8b86d6f06d917f64a&country=MG&year=2022&month=01&day=01")
print(rsp.status_code)
print(rsp.text)
print(rsp.json())
"""
import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"Antananarivo","days":"14"}
headers = {
	    "X-RapidAPI-Key": "3ee5845b4cmsh27d978b5dfc3090p119f03jsn40de6a1152b7",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"}

response = requests.get(url, headers=headers, params=querystring)
clima = response.json()
print(clima)


