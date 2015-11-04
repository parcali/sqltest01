# SELECT statement

# import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	# use a loop to iterate theough database 
	# print line by line 
	for row in c.execute("SELECT city,state from population"):
		print row

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("SELECT city,state from population")
	
	# fetcall() retrieves all records from query
	rows = c.fetchall()

	#output the rows to screen 
	for r in rows:
		print r[0], r[1]
