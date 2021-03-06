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

    return row


def get_students():
    """Get all students."""

    QUERY = """
        SELECT first_name, last_name, github
        FROM students
        """

    db_cursor = db.session.execute(QUERY)

    rows = db_cursor.fetchall()

    if not rows:
        return

    return rows


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


def make_new_project(title, description, max_grade):
    """Add a new project and print confirmation.

    Given a title, description, and max grade, add project to the
    database and print a confirmation message.
    """

    try:
        QUERY = """
                INSERT INTO projects (title, description, max_grade)
                VALUES (:title, :description, :max_grade)
                """

        db.session.execute(QUERY, {'title': title,
                                   'description': description,
                                   'max_grade': max_grade})
        db.session.commit()

        print "Successfully added project: {title}".format(
            title=title)

    except exc.IntegrityError:
        print "Project exists with title \"{}\".".format(title)

    except BaseException as e:
        print "Error in make_new_project(): ", e


def get_project_by_title(title):
    """Given a project title, print information about the project."""

    QUERY = """
        SELECT title, description, max_grade
        FROM Projects
        WHERE title = :title
        """

    db_cursor = db.session.execute(QUERY, {'title': title})

    row = db_cursor.fetchone()

    if not row:
        return

    print "Title: {title}".format(title=row[0])
    print "Description: {description}".format(description=row[1])
    print "Max Grade: {max_grade}".format(max_grade=row[2])

    return row


def get_projects():
    """Get all projects."""

    QUERY = """
        SELECT title, description, max_grade
        FROM Projects
        """

    db_cursor = db.session.execute(QUERY)

    rows = db_cursor.fetchall()

    if not rows:
        return

    return rows


def get_grade_by_github_title(github, title):
    """Print grade student received for a project."""

    QUERY = """
        SELECT grade
        FROM Grades
        WHERE student_github = :github
          AND project_title = :title
        """

    db_cursor = db.session.execute(QUERY, {'github': github, 'title': title})

    row = db_cursor.fetchone()

    if not row:
        return

    print "Student {acct} in project {title} received grade of {grade}".format(
        acct=github, title=title, grade=row[0])

    return row


def assign_grade(github, title, grade):
    """Assign a student a grade on an assignment and print a confirmation."""

    QUERY = """
        INSERT INTO Grades (student_github, project_title, grade)
          VALUES (:github, :title, :grade)
        """

    db.session.execute(QUERY, {'github': github,
                               'title': title,
                               'grade': grade})

    db.session.commit()

    print "Successfully assigned grade of {grade} for {acct} in {title}".format(
        grade=grade, acct=github, title=title)


def get_grades_by_github(github):
    """Get a list of all grades for a student by their github username"""

    QUERY = """
        SELECT project_title, grade
        FROM Grades
        WHERE student_github = :github
        """

    db_cursor = db.session.execute(QUERY, {'github': github})

    rows = db_cursor.fetchall()

    if not rows:
        return

    for row in rows:
        print "Student {acct} received grade of {grade} for {title}".format(
            acct=github, grade=row[1], title=row[0])

    return rows


def get_grades_by_title(title):
    """Get a list of all student grades for a project by its title"""

    QUERY = """
        SELECT student_github, grade
        FROM Grades
        WHERE project_title = :title
        """

    db_cursor = db.session.execute(QUERY, {'title': title})

    rows = db_cursor.fetchall()

    if not rows:
        return

    for row in rows:
        print "Student {acct} received grade of {grade} for {title}".format(
            acct=row[0], grade=row[1], title=title)

    return rows


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

        elif command == "project":
            title = args[0]
            get_project_by_title(title)

        elif command == "grade":
            github, title = args
            get_grade_by_github_title(github, title)

        elif command == "assign_grade":
            github, title, grade = args
            assign_grade(github, title, grade)

        elif command == "student_grades":
            github = args[0]
            get_grades_by_github(github)

        elif command == "project_grades":
            title = args[0]
            get_grades_by_title(title)

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
