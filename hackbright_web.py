"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright_ours as hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    student = hackbright.get_student_by_github(github)

    if not student:
        return "There is no student with github \"{}\".".format(github)

    first, last, github = hackbright.get_student_by_github(github)
    return "{acct} is the GitHub account for {first} {last}".format(
        acct=github, first=first, last=last)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
