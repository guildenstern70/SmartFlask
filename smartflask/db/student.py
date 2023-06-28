#
#  SmartFlask Project
#
#  Copyright (c) 2023 Alessio Saltarin
#  This software is distributed under ISC License.
#  See LICENSE.
#

class Student:
    """ Model class of 'student' table """
    def __init__(self, row):
        self.id = row.id
        self.fullname = row.full_name
        self.email = row.email
        self.birthdate = row.birth_date
        self.number_of_courses = row.number_of_courses

    def __str__(self):
        return "Student: " + self.fullname + " (" + self.email + ")"




