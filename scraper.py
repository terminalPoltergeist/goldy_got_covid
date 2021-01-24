# note for readers:
# double hashtags "##" denote a comment
# single hastags "#" denote code not to run


import requests
# module for api GET requests
import json
# module for handling JSON data from APIs
from datetime import date

# current mn covid data (all JSON data from the state)
mn_current = requests.get(
    "https://api.covidtracking.com/v1/states/mn/current.json?date")
# historical mn covid data (all JSON data from the state)
# mn_historic = requests.get(
#    "https://api.covidtracking.com/v1/states/mn/daily.json")

##
mn_current_dict = json.loads(mn_current.text)
date_now = (mn_current_dict["date"])


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


#print('current data')
jprint(mn_current.json())
#print('historical data')
# jprint(mn_historic.json())

dt = str(date.today())
today = int(dt.replace("-", ""))

if date_now >= today:
    print("works")
