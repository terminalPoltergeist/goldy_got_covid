# note for readers:
# single hashtags "#" denote a comment
# hastag slash "#/" denote code not to run

import requests
# module for api GET requests
import json
# module for handling JSON data from APIs
from datetime import date, timedelta
# date and time madule
from bs4 import BeautifulSoup
# web scraper library


#
# --- Minnesota Covid data api access ---


# current mn covid data (all JSON data from the state)
mn_current = requests.get(
    "https://api.covidtracking.com/v1/states/mn/current.json?date")
#/ historical mn covid data (all JSON data from the state)
#/ mn_historic = requests.get(
#/   "https://api.covidtracking.com/v1/states/mn/daily.json")


# parses JSON response as a Python dictionary
mn_current_dict = json.loads(mn_current.text)
# gets the current date object from the dictionary
date_now = str(mn_current_dict["date"])
cases_today = (mn_current_dict["positiveIncrease"])
cases_total = (mn_current_dict["positive"])
deaths_today = (mn_current_dict["deathIncrease"])
deaths_total = (mn_current_dict["death"])
date_now = (date_now[2:])


#/ def jprint(obj):
# create a formatted string of the Python JSON object
#/    text = json.dumps(obj, sort_keys=True, indent=4)
#/    print(text)


# prints JSON formatted data
#/ jprint(mn_current.json())
#/ jprint(mn_historic.json())


#
# --- metadata setup ---


# gets today's date in form YYYY-MM-DD, conversts to str
dt = date.today()
today = str(dt.strftime('%y%m%d'))
# removes dashes, formats as YYYYMMDD, converts back to int
today = today.replace("-", "")
# calculates yesterday's date and formats it as MM/DD/YY
yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.strftime('%y%m%d')
#/ print(today, yesterday)


#
# --- UMN covid data scraping ---

URL = "https://safe-campus.umn.edu/return-campus/covid-19-dashboard"
dashboard = requests.get(URL).text
#/ data = html.fromstring(dashboard.content)
#/ num = data.xpath(
#/    '//*[@id="block-folwell-content"]/article/div/div[1]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]')
soup = BeautifulSoup(dashboard, "lxml")
cases = soup.findAll(
    "div", class_="field field--name-field-number-of-cases field--type-float field--label-hidden field__item")
U_cases_week = int(cases[7].string.replace(",", ""))
U_cases_total = int(cases[6].string.replace(",", ""))

percentages = soup.findAll(
    "div", class_="field field--name-field-percentage-positive-test field--type-float field--label-hidden field__item")
percent_total = float(percentages[0].string)
percent_week = float(percentages[1].string)

# gets MAG step
URL = "https://housing.umn.edu"
page = requests.get(URL).text
soup = BeautifulSoup(page, "html.parser")
#/ html = soup.find(class_="text")
step = soup.find(class_='text')
step_text = step.find('h2').text


#
# --- Data formatting ---

# makes a dictionary of the data pulled so it can be used in JSON
data = {}
data['mn_cases_today'] = cases_today
data['mn_cases_total'] = cases_total
data['mn_deaths_today'] = deaths_today
data['mn_deaths_total'] = deaths_total
data['ucases_week'] = U_cases_week
data['ucases_total'] = U_cases_total
data['total_percent'] = percent_total
data['week_percent'] = percent_week
data['step'] = step_text
data['prompt1'] = "Stay Home - Doors are monitored after 10 pm."


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile, indent=4)
