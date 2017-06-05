import tweepy
from access import *
from random import randint
import re, time

def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()

    # Set waiting time:
    segs = 3

    # Set wait time:
    tweetlist = ["This is a #Python test for my @pythondaymx workshop. \n#PythonDayMX17",
                "This is anoter automated tweet with #Python for my @pythondaymx workshop. \n#PythonDayMX17",
                "Final automated tweet test for my @pythondaymx workshop. \n#PythonDayMX17"]

    # Eternal posting:
    for tweet in tweetlist:
        # Extract status:
        print(tweet)

        # Try to post tweet:
        try:
            bot.update_status(tweet)
            print("Done")
        except tweepy.TweepError as e:
            print(e.reason)

        # Wait till next sentence extraction:
        time.sleep(segs)
