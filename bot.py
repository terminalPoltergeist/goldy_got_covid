import tweepy
import keys
import json
import post_writer
from datetime import datetime

# api authentication
api_key = keys.api_key
api_secret = keys.api_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret
api_url = "https://api.twitter.com/1.1/statuses/update.json"
# authenticate api
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# create the api object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


time = datetime.now()
time = int(time.strftime("%H"))

if time <= 12:
    post_writer.morning_post()
    status = post_writer.morning_POST
    update = api.update_status(status)
elif time >= 13:
    post_writer.night_post()
    status = post_writer.night_POST
    update = api.update_status(status)

print(update)

# setting the id to the status id number ex. 1354266511159029762
#/id = update.id


# creating an api object to pull tweet data as JSON
#/api_json = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit=True,
#/                     wait_on_rate_limit_notify=True)
#/post = api_json.get_status(id)
