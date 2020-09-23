from random import randrange
from flask import Flask, render_template
import socket

app = Flask(__name__)

VERSION = '1.0'

@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('index.html',
                           version=VERSION,
                           name=name,
                           magicnumber=get_magic_number(),
                           runningip=get_ip())


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
