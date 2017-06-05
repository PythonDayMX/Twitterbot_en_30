import tweepy
from access import *
from random import randint
import re, time

def twitter_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def extract_status(path=None):
    if not path:
        return "No book opened!"
    try:
        with open(path, 'r', encoding='ascii', errors='surrogateescape') as book:
            text = book.read()
        if text:
            return search_sentence(text)
    except:
        return "Book not found!"

def search_sentence(text):
    # Initialize status:
    status = 200

    # While we have a long or very short status:
    while not (5 < status < 125):
        # Generate a random number:
        index = randint(0,len(text))
        # print(status)

        #
        init_index = text[index:].find('.') + index + 2
        last_index = text[init_index:].find('.') + init_index + 2
        status = len(text[init_index:last_index])

    sentence = re.sub("\n", " ", text[init_index:last_index])
    return sentence


if __name__ == '__main__':
    # Setup Twitter API:
    bot = twitter_setup()

    # Set waiting time:
    segs = 3

    # Eternal posting:
    while True:
        # Extract status:
        status = extract_status("texto.txt")
        print(status)

        # Try to post status:
        try:
            bot.update_status(status)
            print("Done")
        except tweepy.TweepError as e:
            print(e.reason)

        # Wait till next sentence extraction:
        time.sleep(segs)
