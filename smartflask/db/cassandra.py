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

    def delete_student(self, student_id):
        query = "DELETE FROM student WHERE id = %s"
        statement = SimpleStatement(query, fetch_size=10)
        self._session.execute(statement, [student_id])
        return True

    def add_student(self, student_dict):
        # Get next id
        query = "SELECT count(*) FROM student"
        statement = SimpleStatement(query, fetch_size=1)
        row = self._session.execute(statement).one()
        next_id = int(row[0]) + 2
        id = "AXS_00" + str(next_id)
        number_of_courses = int(student_dict['numberofcourses'])
        query = "INSERT INTO student (id, full_name, email, birth_date, number_of_courses) VALUES (%s, %s, %s, %s, %s)"
        self._session.execute(query, (id,
                                      student_dict['fullname'],
                                      student_dict['email'],
                                      student_dict['birthdate'],
                                      number_of_courses))
        return True
