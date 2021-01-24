from scraper import today, yesterday, date_now

message = "Data last updated: "

if date_now == today:
    message = message + str(today)
    print(message)
elif date_now + 1 == today:
    message = message + yesterday
    print(message)
