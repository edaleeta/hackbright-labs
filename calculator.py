"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
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


while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")
    if tokens[0] == "q":
        break
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
        else:
            print "Try again!  I don't recognize that math."
