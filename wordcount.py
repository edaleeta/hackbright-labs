# put your code here.
"""
initialize dictionary
open the file
split it on any space
iterate over the list
use .get to check if word is in the dictionary
if it is, we'll increment the current value by 1

print dictionary with the format, key " " value
"""
from sys import argv
from collections import Counter


# TODO: Fix bug where punctuation in the middle of a word
#       is being stripped from the word

# def get_word_count(file_name):
#     """Prints word count of given file"""
#     word_count = {}
#     # document = open(file_name)

#     with open(file_name) as document:

#         for line in document:
#             line = line.rstrip()
#             words = line.split()
#             for word in words:
#                 word = word.lower()
#                 if word.isalnum():
#                     word_count[word] = word_count.get(word, 0) + 1
#                 else:
#                     new_word = ""
#                     for character in word:
#                         if character.isalnum():
#                             new_word += character
#                     word_count[new_word] = word_count.get(new_word, 0) + 1

#     for word, count in word_count.iteritems():
#         print word, count

def get_word_count(file_name):
    document = open(file_name)
    document_contents = document.read()

    words = document_contents.split()

    c = Counter()

    for word in words:
        word = word.lower()
        if word.isalnum():
            c[word] += 1
        else:
            new_word = ""
            for character in word:
                if character.isalnum():
                    new_word += character
            c[new_word] += 1

    document.close()

    sorted_words = sorted(c.keys())

    for word in sorted_words:
        print word, c[word]

get_word_count(argv[1])
