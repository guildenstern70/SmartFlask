#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#


from random import randrange
from flask import Flask, render_template
import socket
import os

app = Flask(__name__)
VERSION = '1.0'


@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):
    context = {
        "version": VERSION,
        "version_name": get_version_name(),
        "environment": get_environment_name(),
        "name": name,
        "magicnumber": get_magic_number(),
        "runningip": get_ip(),
    }
    return render_template('index.html',
                           context=context)


@app.route('/health')
def health():
    return 'I am healthy'


@app.route('/ready')
def ready():
    return 'I am ready.'


def get_magic_number():
    return randrange(0, 1000000000, 2)


def get_ip():
    return socket.gethostbyname(socket.gethostname())


def get_environment_name():
    env_name = get_env_var('ENVIRONMENT')
    if env_name is None:
        env_name = 'Dev'
    return env_name


def get_version_name():
    ver_name = get_env_var('VERSION_NAME')
    if ver_name is None:
        ver_name = 'Dev'
    return ver_name


def get_env_var(var_name):
    var_var = "?"
    try:
        var_var = os.environ[var_name]
    except KeyError:
        pass
    return var_var


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
