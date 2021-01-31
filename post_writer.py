import json

from scraper import today, yesterday, date_now

with open('data.txt') as json_file:
    data = json.load(json_file)


def night_post():
    global night_POST
    step = str(data["step"])
    prompt = str(data["prompt1"])
    night_POST = "We are currently in " + str(step) + " of the Maroon and Gold Sunrise Plan.\n" + str(prompt) + "\n\nCampus COVID data for the week: \nNew Cases: " + str(data["ucases_week"]) + "\nTotal Cases: " + str(
        data["ucases_total"]) + "\nWeek positive test %: " + str(data["week_percent"]) + " % " + "\nTotal positive test %: " + str(data["total_percent"]) + "%"


def morning_post():
    global morning_POST
    message = "(Data current as of "
    if date_now == today:
        message = message + "today)"
        #/ print(message)
    elif date_now + 1 == today:
        message = message + "yesterday)"
        #/ print(message)
    morning_POST = "Minnesota COVID Data:\n\nNew Cases: " + str(data["mn_cases_today"]) + "\nTotal Cases: " + str(
        data["mn_cases_total"]) + "\nNew Deaths: " + str(data["mn_deaths_today"]) + "\nTotal Deaths: " + str(data["mn_deaths_total"]) + "\n" + str(message) + ""


#/ will hold the formatted status update. called in bot.py
# status =

#/ print(data)
