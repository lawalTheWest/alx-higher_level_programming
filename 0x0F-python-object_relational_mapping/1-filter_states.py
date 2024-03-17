#!/usr/bin/python3
'''
    Write a script that:
        lists all states with a name starting with:
            N (upper N)
        from the database:
            hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

'''
    This code should not be executed when imported
'''
if __name__ == '__main__':
    '''
        gets access to the db and get the states.
        Requirements:
            A. script should take 3 arguments:
                1. mysql username, = argv[1]
                2. mysql password = argv[2] and
                3. database name = argv[3]
            B. script should connect to a MySQL server
                running on:
                host = localhost at
                port = 3306
    '''
    db = MySQLdb.connect(host="localhost",
                         port="3306",
                         user=argv[1],
                         password=argv[2],
                         db=argv[3])

    '''
        Create a cursor object:
            more details in the documentation
            (README.md file)
    '''
    cursor_obj = db.cursor()
    cursor_obj.execute("SELECT * FROM states \
                        WHERE name LIKE BINARY 'N%' \
                        ORDER BY states.id ASC")
    rows = cursor_obj.fetchall()
    '''
        iterate through to print the required states
    '''
    for row in rows:
        print(row)

    '''
        close the db and cursor obj
    '''
    cursor_obj.close()
    db.close()
