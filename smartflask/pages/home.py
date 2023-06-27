#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

import smartflask._version as smartflask
import smartflask.utils.environment as utils
from flask import Blueprint, render_template
from smartflask.db import cassandra

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route('/')
def index(name=None):
    context = {
        "version": smartflask.__version__,
        "name": name,
        "cassandra_version": cassandra.version(),
        "magicnumber": utils.magic_number(),
        "runningip": utils.ip(),
    }
    return render_template('index.html',
                           context=context)
