#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement

from smartflask.db.student import Student


def version():
    return cassandra.__version__


class CassandraConnect:
    """ Connect to Cassandra DB"""

    def __init__(self, flask_config, keyspace):
        client_id = flask_config.config["CLIENT_ID"]
        client_secret = flask_config.config["SECRET_KEY"]
        cloud_config = {
            'secure_connect_bundle': 'secure-connect-axscassandradb.zip'
        }
        print("Connecting with Cassandra DB from client " + client_id + "...")
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self._session = cluster.connect()
        self._session.set_keyspace(keyspace)
        print("...connected.")

    def version(self):
        return version()

    def get_students(self):
        query = "SELECT * FROM student"  # users contains 100 rows
        statement = SimpleStatement(query, fetch_size=10)
        students = []
        for user_row in self._session.execute(statement):
            students.append(Student(user_row))
        return students
