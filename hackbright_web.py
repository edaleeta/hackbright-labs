"""A web application for tracking projects, students, and student grades."""

from flask import flash, Flask, redirect, render_template, request

import hackbright_ours as hackbright

app = Flask(__name__)
app.secret_key = "randomstring"


@app.route("/")
def get_homepage():
    """Shows the homepage listing students and projects."""

    projects = hackbright.get_projects()
    students = hackbright.get_students()

    return render_template("homepage.html",
                           students=students,
                           projects=projects)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')
    if not github:
        return "Please enter a student!"

    student = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    if not student:
        return "There is no student with github \"{}\".".format(github)

    first, last, github = student
    # return "{acct} is the GitHub account for {first} {last}".format(
    #     acct=github, first=first, last=last)
    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/new-student", methods=['POST'])
def post_student():
    """Add student to database."""

    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    flash("Successfully added new student.")

    return redirect("/student?github={}".format(github))


@app.route("/new-student")
def get_student_add_form():
    """Show form for adding a student."""

    return render_template("student_add.html")


@app.route("/project")
def get_project():
    """Show information about a project."""

    title = request.args.get('title')
    if not title:
        return "Please enter a title!"

    project = hackbright.get_project_by_title(title)

    grades = hackbright.get_grades_by_title(title)

    if not project:
        return "There is no project with title \"{}\".".format(title)

    title, description, max_grade = project
    return render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade,
                           grades=grades)


@app.route("/project-search")
def get_project_form():
    """Show form for searching for a project."""

    return render_template("project_search.html")


@app.route("/new-project", methods=['POST'])
def post_project():
    """Add project to database."""

    title = request.form.get('title')
    description = request.form.get('description')
    max_grade = request.form.get('max_grade')

    hackbright.make_new_project(title, description, max_grade)

    flash("Successfully added new project.")

    return redirect("/project?title={}".format(title))


@app.route("/new-project")
def get_project_add_form():
    """Show form for adding a project."""

    return render_template("project_add.html")


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
