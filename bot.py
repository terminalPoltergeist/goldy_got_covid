import tweepy
import keys

api_key = keys.api_key
api_secret = keys.api_secret
access_token = keys.access_token
access_token_secret = keys.access_token_secret

# Authenticate to Twitter
auth = tweepy.OAuthHandler("api_key", "api_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)
api.create_friendship("realpython")
