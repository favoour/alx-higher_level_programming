#!/usr/bin/python3
"""a script that lists all cities from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to MySQL server and list cities"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """Execute SQL query"""
    cur.execute("SELECT cities.id, cities.name, states.name\
                 FROM cities LEFT JOIN states\
                 ON states.id = cities.state_id\
                 ORDER BY cities.id ASC")

    """Fetch all rows"""
    cities = cur.fetchall()

    """Print the cities"""
    for city in cities:
        print(city)

    """Close cursor and database connection"""
    cur.close()
    db.close()
