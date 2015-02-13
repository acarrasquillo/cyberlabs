#!/usr/bin/python
# This program is for lab purposes only. This isnt a secure way to implement
# querys in a application because it is open to atacks by SQL Injection

import cgi
import cgitb
cgitb.enable()
import MySQLdb

print """Content-Type: text/html"""
print

# First we create a connection object (db) that represents the database
db = MySQLdb.connect("localhost", "jdelavega", "6TsseuXp", "atackpr_sqlin")

# Once we have a connection with the database, we can create a cursor object (c)
# this cursor will let us use the execute() method to perform SQL commands
c = db.cursor()

form = cgi.FieldStorage()

if form.has_key("num_estudiante"):
	stuNum = form["num_estudiante"].value

	# Try to do an injection here with Union to show the data of all students and professors
	query = """SELECT * FROM User WHERE num_estudiante = "%s" """ % stuNum

	c.execute(query)
	print c.fetchall()

c.close()