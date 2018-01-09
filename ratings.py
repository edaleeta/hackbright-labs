"""
1) Reads the ratings in from the file
2) Stores them in a dictionary
3) And finally, spits out the ratings in alphabetical order by restaurant"""

"""Restaurant rating lister."""

from sys import argv
from random import choice


def organize_restaurant_ratings(file_name):
    """Organizes restaurants and ratings from file into adictionary."""

    restaurant_ratings = {}

    with open(file_name) as document:

        for line in document:
            line = line.rstrip()
            restaurant, rating = line.split(":")
            restaurant_ratings[restaurant] = rating

    return restaurant_ratings

    # restaurants = sorted(restaurant_ratings.keys())

    # for restaurant in restaurants:
    #     print "%s is rated at %s" % (restaurant,
    #                                  restaurant_ratings[restaurant])


def print_sorted(restaurant_ratings):
    """Print restaurants in alphabetical order with rating."""

    print "--- Restaurants and Ratings ---"
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "%s is rated at %s" % (restaurant, rating)


def get_new_restaurant():
    """Asks user for new restaurant and ratings; adds it to dictionary."""

    print "Add a restaurant and rating to the list."
    new_restaurant = raw_input("Give me a restaurant! ")
    new_rating = raw_input("What's its score? ")
    if is_valid_rating(new_rating):
        restaurant_and_ratings[new_restaurant] = new_rating
    else:
        get_new_restaurant()

    print_sorted(restaurant_and_ratings)


def is_valid_rating(rating):
    """Checks if a rating is valid."""
    if rating is None:
        return False
    try:
        if int(rating) < 1 or int(rating) > 5:
            print "Not a valid score"
            return False
    except ValueError:
        print "That's not a number!"
        return False

    return True


def update_random_restaurant():
    """Selects a random restaurant and prompts user for updated rating"""

    random_restaurant = choice(restaurant_and_ratings.keys())
    print "The restaurant is %s.  It's rating is %s" % (random_restaurant, restaurant_and_ratings[random_restaurant])

    new_rating = None
    while not is_valid_rating(new_rating):
        new_rating = raw_input("What should its rating be? ")
        # new_rating_valid = is_valid_rating(new_rating):

    restaurant_and_ratings[random_restaurant] = new_rating


def get_user_interaction():
    """Prompts user for what they want to do."""
    while True:
        print "\nTo see all ratings in alphabetical order type 'A'."
        print "To add and rate a new restaurant type 'B'."
        print "To update a random restaurant's rating type 'C'."
        print "To quit, type 'Q'"
        behavior = raw_input(">> ").lower()

        if behavior == 'a':
            print_sorted(restaurant_and_ratings)
        elif behavior == 'b':
            get_new_restaurant()
        elif behavior == 'c':
            update_random_restaurant()
        elif behavior == 'q':
            quit()
        else:
            print "I didn't understand that!"
            print "Please type 'A', 'B', or 'Q'."

restaurant_and_ratings = organize_restaurant_ratings(argv[1])
get_user_interaction()
