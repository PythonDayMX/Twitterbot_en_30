import tweepy, re, time
from access import *
from random import randint

# Setup API:
# TODO

# Function to extract status (will return status for post):
def extract_status(path=None):
    # No path => return "No book opened!"
    # TODO

    # Try to search a sentence in book:
    try:
        # Open and read textbook:
        # TODO

        # If successfuly read, search sentence:
        # TODO
    except:
        # Book not found:
        # TODO

# Function to search a sentence in book:
def search_sentence(text):
    # Initialize status:
    # TODO

    # While we have a long or very short status:
    while not (5 < status < 125):
        # Generate a random number:
        # TODO

        # Set indices of sentence:
        # TODO

    # Replace breaks w/spaces:
    # TODO


if __name__ == '__main__':
    # Setup Twitter API:
    # TODO

    # Set waiting time:
    segs = 3

    # Eternal posting:
    while True:
        # Extract status:
        # TODO

        # Try to post status:
        # TODO

        # Wait till next sentence extraction:
        time.sleep(segs)
