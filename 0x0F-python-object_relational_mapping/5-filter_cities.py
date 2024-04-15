#!/usr/bin/python3
"""script that lists all cities of a given state from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cur = db.cursor()

    # Get the state from command-line arguments
    state = sys.argv[4]

    # Execute SQL query
    query = ("SELECT cities.id, cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cur.execute(query, (state,))
    cities = cur.fetchall()

    # Print the cities
    for city in cities:
        print(city)

    cur.close()
    db.close()
