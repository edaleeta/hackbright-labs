"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    if tokens[0] == "q":
        quit()
    else:
        if tokens[0] == "+":
            print add(float(tokens[1]), float(tokens[2]))
