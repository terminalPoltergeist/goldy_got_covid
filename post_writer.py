import json

from scraper import today, yesterday, date_now

message = "(Data current as of "

if date_now == today:
    message = message + "today)"
    print(message)
elif date_now + 1 == today:
    message = message + "yesterday)"
    print(message)

with open('data.txt') as json_file:
    data = json.load(json_file)

print(data)
