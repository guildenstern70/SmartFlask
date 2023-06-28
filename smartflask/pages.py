#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

import smartflask._version as smartflask
import smartflask.utils.environment as utils
from flask import Blueprint, render_template, request


def setup_blueprint(cassandra_connection):
    pages = Blueprint('home_page', __name__, template_folder='templates')

    @pages.route('/')
    def index():
        context = {
            "version": smartflask.__version__,
            "cassandra_version": cassandra_connection.version(),
            "magicnumber": utils.magic_number(),
            "runningip": utils.ip(),
        }
        return render_template('index.html',
                               context=context)

    @pages.route('/more')
    def more():
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
