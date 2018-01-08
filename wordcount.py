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


def get_word_count(file_name):
    """Prints word count of given file"""
    word_count = {}
    # document = open(file_name)

    with open(file_name) as document:

        for line in document:
            line = line.rstrip()
            words = line.split()
            for word in words:
                word = word.lower()
                if word.isalnum():
                    word_count[word] = word_count.get(word, 0) + 1
                else:
                    new_word = ""
                    for character in word:
                        if character.isalnum():
                            new_word += character
                    word_count[new_word] = word_count.get(new_word, 0) + 1


    for word, count in word_count.iteritems():
        print word, count


get_word_count("test.txt")
get_word_count("twain.txt")
