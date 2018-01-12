############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name, pairings=None):
        """Initialize a melon."""
        if pairings is None:
            self.pairings = []
        else:
            self.pairings = pairings

        # Fill in the rest

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest

        self.code = new_code

    def __repr__(self):
        return 'MelonType(name={})'.format(self.name)


def make_melon_types(melons):
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest

    for melon in melons:

        code, year, color, is_seedless, is_bestseller, name, pairings = melon
        melontype_object = MelonType(code, year, color, is_seedless,
                                     is_bestseller, name, pairings)
        # for pairing in melon[6]:
        #     melontype_object.add_pairing(pairing)
        all_melon_types.append(melontype_object)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melontype_object in melon_types:
        print "{name} pairs with".format(name=melontype_object.name)
        for pairing in melontype_object.pairings:
            print "- {}".format(pairing)
        print


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melons_dict = {}

    for melontype_object in melon_types:
        melons_dict[melontype_object.code] = melontype_object

    return melons_dict

# Defining our list of tuples for melons
# (self, code, first_harvest, color, is_seedless, is_bestseller, name, pairings)
melons = [('musk', 1998, 'green', True, True, 'Muskmelon', ['mint']),
          ('cas', 2003, 'orange', False, False, 'Casaba', ['strawberries', 'mint']),
          ('cren', 1996, 'green', False, False, 'Crenshaw', ['proscuitto']),
          ('yw', 2013, 'yellow', False, True, 'Yellow Watermelon', ['ice cream'])]

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_id, melon_type, shape_rating, color_rating, harvest_field, harvester):
        """Initialize a Melon."""
        self.melon_id = melon_id
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvester = harvester

    def is_sellable(self):
        """Determines whether or not melon is sellable."""

        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            return True
        return False
    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melons, harvested_melons):
    """Returns a list of Melon objects."""

    melon_objects = []

    melontypes_dict = make_melon_type_lookup(make_melon_types(melons))

    for melon in harvested_melons:
        melon_num, melon_code, shape_rating, color_rating, harvest_field, harvester = melon

        melon_object = Melon(melon_num, melontypes_dict[melon_code],
                        shape_rating, color_rating, harvest_field, harvester)

        melon_objects.append(melon_object)

    for melon in melon_objects:
        print "Melon", melon.melon_id
        print "- Melon type:", melon.melon_type.code
        print "- Shape rating:", melon.shape_rating
        print "- Color rating:", melon.color_rating
        print "- Harvested from Field", melon.harvest_field
        print "- Harvested by", melon.harvester

    return melon_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


harvested_melons = [
                    (1, 'yw', 8, 7, 2, "Sheila"),
                    (2, "yw", 3, 4, 2, "Sheila"),
                    (3, "yw", 9, 8, 3, "Sheila"),
                    (4, "cas", 10, 6, 35, "Sheila"),
                    (5, "cren", 8, 9, 35, "Michael"),
                    (6, "cren", 8, 2, 35, "Michael"),
                    (7, "cren", 2, 3, 4, "Michael"),
                    (8, "musk", 6, 7, 4, "Michael"),
                    (9, "yw", 7, 10, 3, "Sheila")
                    ]


