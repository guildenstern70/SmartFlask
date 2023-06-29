#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

import smartflask._version as smartflask
import smartflask.utils.environment as utils
from flask import Blueprint, render_template, request, flash, session, redirect, url_for


def setup_blueprint(cassandra_connection):
    pages = Blueprint('home_page', __name__, template_folder='templates')

    def _post_student(post_request):
        fullname = post_request.form['fullname']
        email = post_request.form['email']
        birthdate = post_request.form['birthdate']
        numberofcourses = post_request.form['numberofcourses']
        if not fullname:
            flash('Student fullname is required!')
        elif not email:
            flash('Student email is required!')
        elif not birthdate:
            flash('Student birthdate is required!')
        elif not numberofcourses:
            flash('Student number of courses is required!')
        else:
            cassandra_connection.add_student({
                "fullname": fullname,
                "email": email,
                "birthdate": birthdate,
                "numberofcourses": numberofcourses
            })
            return redirect('/more')

    @pages.route('/')
    def index():
        context = {
            "version": smartflask.__version__,
            "cassandra_version": cassandra_connection.version(),
            "magicnumber": utils.magic_number(),
            "runningip": utils.ip(),
        }
        session.pop('_flashes', None)
        return render_template('index.html',
                               context=context)

    @pages.route('/more', methods=['GET', 'POST'])
    def more():
        if request.method == 'POST':
            _post_student(request)
        students = cassandra_connection.get_students()
        context = {
            "version": smartflask.__version__,
            "students": students,
        }
        return render_template('more.html',
                               context=context)

    @pages.route('/delete')
    def delete_stundent():
        student_id = request.args.get('student_id')
        cassandra_connection.delete_student(student_id)
        return more()

    return pages
