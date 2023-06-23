#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#


from flask import Flask, render_template, url_for
import src.utils.environment as utils
from src.db import cassandra

app = Flask(__name__, static_url_path='')
VERSION = '1.0'


@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):
    context = {
        "version": VERSION,
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
    return 'I am healthy'


@app.route('/ready')
def ready():
    return 'I am ready.'


if __name__ == '__main__':
    print("SmartFlask v." + VERSION)
    app.run(host='0.0.0.0', port=8080)
