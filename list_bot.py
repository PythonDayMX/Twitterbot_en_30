import tweepy, time
from access import *
from random import randint

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    # TODO

    # Return API access:
    # TODO

if __name__ == '__main__':
    # Setup Twitter API:
    # TODO

    # Set waiting time:
    secs = 3

    # Set tweet list:
    tweetlist = ["Test tweet using #Python in @FerroRodolfo's workshop at the @pythondaymx \n#PythonDayMX17",
                " \n#PythonDayMX17",
                " \n#PythonDayMX17"]

    # Tweet posting:
    for tweet in tweetlist:
        # Print tweet:
        print(tweet)

        # Try to post tweet:
        # TODO

        # Wait till next sentence extraction:
        time.sleep(secs)
