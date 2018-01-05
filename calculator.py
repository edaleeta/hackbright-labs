"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def print_instructions():
    """"Prints instructions for the calculator."""
    print "Welcome to the Calculator!"
    print "Type \"+ [number] [number]\" to add."
    print "Type \"- [number] [number]\" to subtract."
    print "Type \"* [number] [number]\" to multiply."
    print "Type \"/ [number] [number]\" to divide."
    print "Type \"square [number]\" to square the number."
    print "Type \"cube [number]\" to cube the number."
    print "Type \"pow [number] [number]\" to raise the first number to the power of the second number."
    print "Type \"% [number] [number]\" to get the remainer of the first number divided by the second number."
    print "Type \"q\" to exit the Calculator."


def return_valid_tokens(tokens):
    """Checks to see if user input is valid."""

    param_req = {"+": 2,
                 "-": 2,
                 "*": 2,
                 "/": 2,
                 "square": 1,
                 "cube": 1,
                 "pow": 2,
                 "%": 2}

    if tokens[0] not in param_req:
        print "Sorry, I don't understand that operation.  Try again!"
        return False
    else:
        if param_req[tokens[0]] != (len(tokens)-1):
            print "Sorry. That wasn't the correct amount of numbers for {} operation.".format(tokens[0])
            print "Expected {}".format(param_req[tokens[0]])
            print "Try again."
            return False
        valid_inputs = [tokens[0]]
        for token in tokens[1:]:
            try:
                token = float(token)
                valid_inputs.append(token)
            except ValueError:
                print "Sorry, that wasn't a number.  Try again!"
                return False

        return valid_inputs

print_instructions()
while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    if tokens[0] == "q":
        break
    else:
        tokens = return_valid_tokens(tokens)
        if tokens is False:
            continue
        if tokens[0] == "+":
            print add(tokens[1], tokens[2])
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
        else:
            print "Try again!  I don't recognize that math."
