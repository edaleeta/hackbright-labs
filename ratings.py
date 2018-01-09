"""
1) Reads the ratings in from the file
2) Stores them in a dictionary
3) And finally, spits out the ratings in alphabetical order by restaurant"""

"""Restaurant rating lister."""

from sys import argv


def print_restaurant_ratings(file_name):
    """prints restaurant and its rating from a file"""

    restaurant_ratings = {}

    with open(file_name) as document:

        for line in document:
            line = line.rstrip()
            restaurant, rating = line.split(":")
            restaurant_ratings[restaurant] = rating

    # restaurants = sorted(restaurant_ratings.keys())

    # for restaurant in restaurants:
    #     print "%s is rated at %s" % (restaurant,
    #                                  restaurant_ratings[restaurant])

    for restaurant, rating in sorted(restaurant_ratings.items()):
        print "%s is rated at %s" % (restaurant, rating)


print_restaurant_ratings(argv[1])
