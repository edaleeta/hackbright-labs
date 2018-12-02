from sys import argv
from collections import Counter
from operator import itemgetter


def get_word_count(file_name):
    """Reads in a file and prints frequency of each word found."""

    with open(file_name) as document:
        document_contents = document.read()

    words = document_contents.split()
    index_deletions = []

    # Cleans words
    for index, word in enumerate(words):
        if word == "":
            continue

        # While the last char of the word is not alnum, strip that char.
        try:
            while not word[-1].isalnum():
                word = word[:-1]
        except IndexError:
            # No chars are valid; mark for deletion.
            index_deletions.append(index)
            continue

        # While first char is the word is not alnum, strip that char.
        while not word[0].isalnum():
            word = word[1:]

        # Word count ignores capitalization.
        word = word.lower()

        words[index] = word

    # Deletes invalid words; reversed to prevent index shifting.
    for index in reversed(index_deletions):
        del words[index]

    word_count = Counter(words)

    sorted_word_count = sorted(word_count.items(), key=itemgetter(0))
    sorted_word_count = sorted(sorted_word_count,
                               key=itemgetter(1), reverse=True)

    for word, count in sorted_word_count:
        print word, count

get_word_count(argv[1])
