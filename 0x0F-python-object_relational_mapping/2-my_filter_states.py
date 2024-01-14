#!/usr/bin/python3
'''
    displays all values in the states
'''

import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''
        Access to the database and get the states
        from the database.
    '''

    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         port=3306,
                         passwd=argv[2],
                         db=argv[3])

    cursor_obj = db.cursor()
    cursor_obj.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cursor_obj.fetchall()

    for row in rows:
        print(row)
