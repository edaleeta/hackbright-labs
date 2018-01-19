"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    # __init__ (first-name, last-name, email, password)
    # initialize with these values

    def __init__(self, first_name, last_name, email, password):
        """Initializes a customer."""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    # __repr__:
    # return "<Customer: {name}, {email}>".format(addhere)"

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {f} {l}, email: {e}>".format(f=self.first_name,
                                                        l=self.last_name,
                                                        e=self.email)

    # def read_customers_from_file(filepath):
    # creates dictionary with customer data


def read_customers_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: Customer object}"""

    customer_dict = {}

    with open(filepath) as customer_data:
        for line in customer_data:
            (first_name,
             last_name,
             email,
             password) = line.strip().split("|")

            customer_dict[email] = Customer(first_name,
                                            last_name,
                                            email,
                                            password)

    return customer_dict


    # def get_by_email:
    # Returns a customer object by email address
