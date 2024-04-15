#!/usr/bin/python3
"""Script that takes in an arg and displays all values in the states table"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to MySQL server and display values"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """Format and execute SQL query"""
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
             "ORDER BY states.id ASC").format(sys.argv[4])
    cur.execute(query)

    """Fetch all rows"""
    states = cur.fetchall()

    """Print the states"""
    for state in states:
        print(state)

    """Close cursor and database connection"""
    cur.close()
    db.close()
