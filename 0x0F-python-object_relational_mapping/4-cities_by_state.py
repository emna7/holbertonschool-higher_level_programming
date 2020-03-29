 #!/usr/bin/python3
"""
"""
import sys
import MySQLdb
if __name__ == "__main__":
    usa_db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    cur = usa_db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON (cities.state_id = states.id) \
                ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print("{}".format(row))
    cur.close()
    usa_db.close()
