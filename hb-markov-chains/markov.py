"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(files):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_document = []
    # your code goes here
    for filename in files:

        with open(filename) as document:
            full_document.append(document.read())

    return " ".join(full_document)


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    words.append(None)

    for i in range(len(words) - n):
        new_tuple = tuple(words[i:i+n])

        if new_tuple in chains:
            chains[new_tuple].append(words[i + n])
        else:
            chains[new_tuple] = [words[i + n]]
    return chains


def make_text(chains):
    """Return text from chains."""
    punctuation = [".", "?", "!"]

    while True:
        link = choice(chains.keys())
        if link[0][0].isupper():
            break

    words = list(link)

    while True:
        next_word = choice(chains[link])
        if not next_word:
            break

        words.append(next_word)
        link = tuple(words[-n:])

    if words[-1][-1] not in punctuation:
        words[-1] = words[-1] + choice(punctuation)

    return " ".join(words)


n = int(sys.argv[1])  # number for n-grams

input_path = sys.argv[2:]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
