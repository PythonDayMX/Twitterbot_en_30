import tweepy, re, time
from access import *
from random import randint

# Setup API:
def twitter_setup():
    # Authenticate and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API access:
    api = tweepy.API(auth)
    return api

# Function to extract status (will return status for post):
def extract_status(path=None):
    # No path => return "No book opened!"
    if not path:
        return "No book opened!"

    # Try to search a sentence in book:
    try:
        # Open and read textbook:
        with open(path, 'r', encoding='ascii', errors='surrogateescape') as book:
            text = book.read()
        # If successfuly read, search sentence:
        if text:
            return search_sentence(text)
    except:
        # Book not found:
        return "Book not found!"

# Function to search a sentence in book:
def search_sentence(text):
    # Initialize status:
    status = 200

    # While we have a long or very short status:
    while not (5 < status < 125):
        # Generate a random number:
        index = randint(0,len(text))
        # print(status)

        # Set indices of sentence:
        init_index = text[index:].find('.') + index + 2
        last_index = text[init_index:].find('.') + init_index + 2
        status = len(text[init_index:last_index])

    # Replace breaks w/spaces:
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
            print("Successfully posted.")
        except tweepy.TweepError as e:
            print(e.reason)

        # Wait till next sentence extraction:
        time.sleep(segs)
