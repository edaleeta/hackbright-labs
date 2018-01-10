"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""

def is_anagram(brackets):
    """Tests to see if list is an anagram."""

    reversed_brackets = {'(': ')', '{': '}', '[': ']', '<': '>',
                         ')': '(', '}': '{', ']': '[', '>': '<'}

    reversed_and_flipped = [reversed_brackets[bracket] for bracket in brackets[::-1]]

    if reversed_and_flipped == brackets:
        return True
    return False


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """

    brackets = ['(', ')', '{', '}', '[', ']', '<', '>']

    brackets_in_phrase = []

    """march through phrase, look for bracket.
    if we find a bracket, let's test to see if it's an anagram"""

    for letter in phrase:
        if letter in brackets:
            brackets_in_phrase.append(letter)

    if len(brackets_in_phrase) % 2 == 1:
        return False
    return is_anagram(brackets_in_phrase)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n"
