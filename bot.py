import tweepy
import api_keys

# Authenticate to Twitter
auth = tweepy.OAuthHandler("api_key", "api_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
