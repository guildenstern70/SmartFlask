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


def environment_name():
    env_name = env_var('ENVIRONMENT')
    if env_name is None:
        env_name = 'Dev'
    return env_name


def version_name():
    ver_name = env_var('VERSION')
    if ver_name is None:
        ver_name = 'Dev'
    return ver_name



