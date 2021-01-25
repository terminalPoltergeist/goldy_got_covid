# note for readers:
# single hashtags "#" denote a comment
# hastag slash "#/" denote code not to run

import requests
# module for api GET requests
import json
# module for handling JSON data from APIs
from datetime import date, timedelta

# current mn covid data (all JSON data from the state)
mn_current = requests.get(
    "https://api.covidtracking.com/v1/states/mn/current.json?date")
#/ historical mn covid data (all JSON data from the state)
#/ mn_historic = requests.get(
#/   "https://api.covidtracking.com/v1/states/mn/daily.json")

# parses JSON response as a Python dictionary
mn_current_dict = json.loads(mn_current.text)
# gets the current date object from the dictionary
date_now = (mn_current_dict["date"])
cases_today = (mn_current_dict["positiveIncrease"])
cases_total = (mn_current_dict["positive"])
deaths_today = (mn_current_dict["deathIncrease"])
deaths_total = (mn_current_dict["death"])


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# prints JSON formatted data
jprint(mn_current.json())
#/ jprint(mn_historic.json())

# gets today's date in form YYYY-MM-DD, conversts to str
dt = str(date.today())
# removes dashes, formats as YYYYMMDD, converts back to int
today = int(dt.replace("-", ""))
# calculates yesterday's date and formats it as MM/DD/YY
yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.strftime('%m/%d/%y')
