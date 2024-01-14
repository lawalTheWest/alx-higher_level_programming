#!/usr/bin/python3
'''
    script that lists all states with a name starting with N
    (upper N) from the database hbtn_0e_0_usa
'''


import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''
        Access $ retrieves states from database.
    '''
    db = MySQLdb.connect(host="localhost",  # MySQL server host
                         user=argv[1],  # username
                         port=3306,  # port
                         passwd=argv[2],  # user password
                         db=argv[3]  # the database name
                         )
    '''
        creating a cursor object to retrieve data
    '''
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row) # ends for
