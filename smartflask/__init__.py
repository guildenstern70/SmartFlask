#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

import os
import smartflask._version as smartflask
from flask import Flask
from smartflask.db import cassandra
from smartflask.db.cassandra import CassandraConnect
from smartflask import pages


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__,
                instance_relative_config=True,
                static_url_path='')
    app.config.from_prefixed_env()

    print("Smark Flask v." + smartflask.__version__)

    cassandra_conn = CassandraConnect(app, 'smartflaskks')
    app.register_blueprint(pages.setup_blueprint(cassandra_conn))

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

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
