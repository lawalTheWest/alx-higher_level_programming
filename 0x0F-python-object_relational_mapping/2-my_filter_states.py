#!/usr/bin/python3
'''
    This script takes in an argument
    and displays all values in the states table of
    the db (hbtn_0e_0_usa) where name matches argument.
'''


import MySQLdb
from sys import argv

'''
    Code should not be executed when imported
'''


if __name__ == '__main__':
    '''
        Accesses the db and get the states
    '''
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    '''
        Creating a cursor object to access the db
    '''
    cursor_obj = db.cursor()
    cursor_obj.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY '{}' \
                        ORDER BY states.id ASC".format(argv[4]))
    rows = cursor_obj.fetchall()

    for row in rows:
        print(row)
