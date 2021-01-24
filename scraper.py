import requests
# module for api GET requests

mn_current = requests.get(
    "https://api.covidtracking.com/v1/states/mn/current.json")
mn_historic = requests.get(
    "https://api.covidtracking.com/v1/states/mn/daily.json")

print(mn_historic.json())
