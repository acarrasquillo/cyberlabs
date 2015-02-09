# This program is for lab purposes only. This isnt a secure way to implement
# querys in a application because it is open to atacks by SQL Injection

import MySQLdb

# First we create a connection object (db) that represents the database
db = MySQLdb.connect("localhost", "jdelavega", "6TsseuXp", "atackpr_sqlin")

# Once we have a connection with the database, we can create a cursor object (c)
# this cursor will let us use the execute() method to perform SQL commands
c = db.cursor()

user = raw_input('Username: ')
passw = raw_input('Password: ')

# The injection can be made by making username and password true
c.execute("""SELECT * FROM User WHERE username = "%s" AND password = "%s" """ % (user, passw))

print c.fetchall()

c.close()
