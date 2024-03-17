#!/usr/bin/python3
'''
    Write a script that:
        lists all states from the database:
            hbtn_0e_0_usa:
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
                1. mysql username,
                2. mysql password and
                3. database name
            B. script should connect to a MySQL server
                running on localhost at port 3306
    '''
    db = MySQLdb.connect(host="localhost",
                            user=argv[1],
                            port="3306",
                            password=argv[2],
                            db=argv[3])

    '''
        Creating a cursor object for my_db:
            more details in the documentation file
            README.md
    '''
    db_cursor_obj = db.cursor()
    db_cursor_obj.execute("SELECT * FROM states")
    rows = db_cursor_obj.fetchall()

    '''
        Iterate through the db and print all the states
    '''
    for row in rows:
        print(row)

    '''
        Close the cursor and database connection
    '''
    db_cursor_obj.close()
    db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        exit(1)
