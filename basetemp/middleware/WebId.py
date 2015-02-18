__author__ = 'travisselland'

from django.db import connection

def get_next():
    i = 0
    while True:
        # create unique id and yield it to requesting function
        i += 1
        yield "webID_" + str(i)

def sql_sequence(self):
    cursor = connection.cursor()

    cursor.execute("SELECT nextval('serial');")
    row = cursor.fetchone()
    print(row)

    #if the request ID number gets close to its limit, restart at 101
    # upper limit = 9223372036854775807 source: http://www.postgresql.org/docs/9.4/static/sql-createsequence.html
    if row >= 9223372036854775800:
        cursor.execute("ALTER SEQUENCE serial restart 101;")

    return row

    #I was going to incorporate the above function, linking the id's to the database, but I ran out of energy
    # and didn't see the need to pursue it further.


# in the middleware
class WebIDMiddleware(object):
    def process_request(self, request):
        try:
            next(request.session.generator)
            # sql_sequence(self)
        except AttributeError:
            request.session.generator = get_next()
            # sql_sequence(self)