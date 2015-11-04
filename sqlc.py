# INSERT COMMAND

# import the sqlite3 library
import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#insert multiple values as tuple
	cities = [
	('Boston','MA',600000),('Chicago','IL',2700000),
	('Houston','TX',2100000),('Phonex','AZ',1500000)
	]

	#insert data into table
	c.executemany("INSERT INTO population VALUES(?,?,?)",cities)
