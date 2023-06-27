#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

from random import randrange
import socket
import os


def magic_number():
    return randrange(0, 1000000000, 2)


def ip():
    return socket.gethostbyname(socket.gethostname())


def env_var(var_name):
    var_var = "?"
    try:
        var_var = os.environ[var_name]
    except KeyError:
        pass
    return var_var




