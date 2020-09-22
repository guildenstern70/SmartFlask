from random import randrange
from flask import Flask, render_template
import socket

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('index.html',
                           name=name,
                           magicnumber=get_magic_number(),
                           runningip=get_ip())


def get_magic_number():
    return randrange(0, 1000000000, 2)


def get_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == '__main__':
    app.run()
