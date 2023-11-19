#!/usr/bin/python3

'''
    Lists all states from the datyabase 'hbtn_0e_0_usa'
'''


import MySQLdb
from sys import argv


if __name__ == '__main__':
    '''
        access the database (db) and retrieve states.
        database name = hbtn_0e_0_usa
        for this task no argument validation are required
    '''
    db = MySQLdb.connect(host='localhost',  # database host
                         user=argv[1],  # MySQL username
                         port=3306,  # MySQL server port
                         password=argv[2],  # MySQL password
                         db=argv[3]  # MySQL database name to connect to
                         )
    '''
        create a cursor object to iterate & retrieve data from db
    '''
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
