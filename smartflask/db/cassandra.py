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


def version():
    return cassandra.__version__


class CassandraConnect:
    """ Connect to Cassandra DB"""
    def __init__(self, flask_config):
        client_id = flask_config.config["CLIENT_ID"]
        client_secret = flask_config.config["SECRET_KEY"]
        cloud_config = {
            'secure_connect_bundle': 'secure-connect-axscassandradb.zip'
        }
        print("Connecting with Cassandra DB from client " + client_id)
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self._session = cluster.connect()
        self._session.set_keyspace("firstkeyspace")
        print("...connected.")

    def get_employees(self):
        query = "SELECT * FROM employee"  # users contains 100 rows
        statement = SimpleStatement(query, fetch_size=10)
        for user_row in self._session.execute(statement):
            print(user_row)


