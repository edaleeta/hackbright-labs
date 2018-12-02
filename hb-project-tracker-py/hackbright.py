"""Hackbright Project Tracker.

A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

app = Flask(__name__)
db = SQLAlchemy()


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///hackbright'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


def get_student_by_github(github):
    """Given a GitHub account name, print info about the matching student."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        WHERE github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    row = db_cursor.fetchone()

    if row:
        print "Student: {first} {last}\nGitHub account: {acct}".format(
            first=row[0], last=row[1], acct=row[2])
    else:
        print "No student found with github \"" + github + "\"."


def make_new_student(first_name, last_name, github):
    """Add a new student and print confirmation.

    Given a first name, last name, and GitHub account, add student to the
    database and print a confirmation message.
    """

    try:
        QUERY = """
                INSERT INTO students (first_name, last_name, github)
                VALUES (:first_name, :last_name, :github)
                """

        db.session.execute(QUERY, {'first_name': first_name,
                                   'last_name': last_name,
                                   'github': github})
        db.session.commit()

        print "Successfully added student: {first} {last}".format(
            first=first_name, last=last_name)

    except exc.IntegrityError:
        print "Student exists with github \"{}\".".format(github)

    except BaseException as e:
        print "Error in make_new_student(): ", e


def get_project_by_title(title):
    """Given a project title, print information about the project."""
    pass


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""
    pass


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""
    pass


def is_bad_args(num_args, req_args, msg=None):
    """Checks if user entered the required number of args for command."""
    # If num args less than req args say you need req_args

    if num_args < req_args:

        if msg:
            print msg

        else:
            print "Please enter {} arguments.".format(req_args)

        return True
    return False


def handle_input():
    """Main loop.

    Repeatedly prompt for commands, performing them, until 'quit' is received as a
    command."""

    QUIT_COMMANDS = ['quit', 'q']

    command = None

    while command not in QUIT_COMMANDS:
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split()
        command = tokens[0].lower()
        args = tokens[1:]
        num_args = len(args)

        if command == "student":
            bad_msg = "Please enter student github after \"student\"."

            if is_bad_args(num_args, 1, bad_msg):
                continue

            github = args[0]
            get_student_by_github(github)

        elif command == "new_student":
            if is_bad_args(num_args, 3):
                continue

            first_name, last_name, github = args  # unpack!
            make_new_student(first_name, last_name, github)

        else:
            if command not in QUIT_COMMANDS:
                print "Invalid Entry. Please enter quit, student, or new_student."


if __name__ == "__main__":
    #try:
    connect_to_db(app)

    handle_input()

    # To be tidy, we close our database connection -- though,
    # since this is where our program ends, we'd quit anyway.

    #except:
    #handle exceptions

    #finally:
    db.session.close()
