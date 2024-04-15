#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """Execute the query to fetch all states"""
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """query states"""
    rows = cur.fetchall()

    """Print the states"""
    for row in rows:
        print(row)

    """Close cursor and database connection"""
    cur.close()
    db.close()
