#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

import os
from flask import Flask, render_template
import smartflask.utils.environment as utils
from smartflask.db import cassandra
from smartflask.db.cassandra import CassandraConnect


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__,
                instance_relative_config=True,
                static_url_path='')
    app.config.from_prefixed_env()

    print("Smark Flask v." + str(app.config["SMARTFLASK_VERSION"]))
    print("- Secret Key = " + app.config["SECRET_KEY"])

    cassandra_conn = CassandraConnect(app)
    employees = cassandra_conn.get_employees()
    print(employees)
    employees = cassandra_conn.get_employees()
    print(employees)
    employees = cassandra_conn.get_employees()
    print(employees)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index(name=None):
        context = {
            "version": app.config["SMARTFLASK_VERSION"],
            "version_name": utils.version_name(),
            "environment": utils.environment_name(),
            "name": name,
            "cassandra_version": cassandra.version(),
            "magicnumber": utils.magic_number(),
            "runningip": utils.ip(),
        }
        return render_template('index.html',
                               context=context)

    @app.route('/health')
    def health():
        return {
            'app': 'SmartFlask',
            'version': app.config["SMARTFLASK_VERSION"],
            'healthy': 'Healthy'
        }

    @app.route('/ready')
    def ready():
        return {
            'app': 'SmartFlask',
            'version': app.config["SMARTFLASK_VERSION"],
            'ready': 'Ready'
        }

    return app
