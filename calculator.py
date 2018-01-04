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
        elif tokens[0] == "-":
            print subtract(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "*":
            print multiply(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "/":
            print divide(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "square":
            print square(float(tokens[1]))
        elif tokens[0] == "cube":
            print cube(float(tokens[1]))
        elif tokens[0] == "pow":
            print power(float(tokens[1]), float(tokens[2]))
        elif tokens[0] == "%":
            print mod(float(tokens[1]), float(tokens[2]))
