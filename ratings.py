"""
1) Reads the ratings in from the file
2) Stores them in a dictionary
3) And finally, spits out the ratings in alphabetical order by restaurant"""

"""Restaurant rating lister."""

from sys import argv


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
    try:
        if int(new_rating) < 1 or int(new_rating) > 5:
            print "Not a valid score"
            get_new_restaurant()
    except ValueError:
        print "That's not a number!"
        get_new_restaurant()
    restaurant_and_ratings[new_restaurant] = new_rating

    print_sorted(restaurant_and_ratings)


restaurant_and_ratings = organize_restaurant_ratings(argv[1])
while True:
    print "\nTo see all ratings in alphabetical order type 'A'."
    print "To add and rate a new restaurant type 'B'."
    print "To quit, type 'Q'"
    behavior = raw_input(">> ").lower()

    if behavior == 'a':
        print_sorted(restaurant_and_ratings)
    elif behavior == 'b':
        get_new_restaurant()
    elif behavior == 'q':
        quit()
    else:
        print "I didn't understand that!"
        print "Please type 'A', 'B', or 'Q'."
