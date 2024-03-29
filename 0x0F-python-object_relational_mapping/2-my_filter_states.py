#!/usr/bin/python3
""" Script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def print_states(argv):
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
            WHERE BINARY name = '{}' ORDER BY states.id ASC""".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    print_states(sys.argv)
