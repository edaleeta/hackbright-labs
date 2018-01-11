"""A Markov chain generator that can tweet random messages."""

import os
import sys
from random import choice
import twitter
import tweet_dumper

TWEET_CHAR_COUNT = 240

def open_and_read_file(filenames):
    """Take list of files. Open them, read them, and return one long string."""

    body = ""

    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    return body


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

        # or we could replace the last three lines with:
        #    chains.setdefault(key, []).append(value)

    return chains


def make_text(chains):
    """Take dictionary of Markov chains; return random text."""

    punctuation = [".", "?", "!"]

    char_count = 0

    while True:
        # Select a random key until we have one that starts with a capital letter.
        key = choice(chains.keys())
        if key[0][0].isupper():
            break

    words = list(key)
    char_count += len(key[0])
    char_count += len(key[1])

    while key in chains and char_count + len(words) < TWEET_CHAR_COUNT:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).
        # OR
        # Until we reach the max Twitter char limit
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        words.append(word)
        char_count += len(word)
        # If the added word puts us over the Twitter limit, pop it off.
        if char_count + len(words) >= TWEET_CHAR_COUNT:
            words.pop()
            break
        key = (key[1], word)

    text = " ".join(words)

    # If our last character isn't a punctuation, add a random one.
    if text[-1] not in punctuation:
        text = text + choice(punctuation)
    return text


def tweet(chains):
    """Create a tweet and send it to the Internet."""

    # Use Python os.environ to get at environmental variables
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.

# Fix this error! UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 2: ordinal not in range(128)
    status = api.PostUpdate(make_text(chains), verify_status_length=False)

api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                  access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# Get the filenames from the user through a command line prompt, ex:
# python markov.py stone.txt phoenix.txt
file_names = sys.argv[1:] 

# Open the files and turn them into one long string

text = open_and_read_file(file_names)

# Get a Markov chain
chains = make_chains(text)

tweet(chains)

