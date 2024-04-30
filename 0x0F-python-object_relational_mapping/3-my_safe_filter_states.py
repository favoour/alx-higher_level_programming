#!/usr/bin/python3
"""Script that takes in an arg and displays all values in the states table"""
import sys
import MySQLdb


if __name__ == "__main__":
    """Connect to the database"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
