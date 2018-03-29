#!/usr/bin/python

import MySQLdb
import sys

connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")

cursor = connection.cursor ()
cursor.execute ("select Domain ,Active, Program, InScope from domains limit 5")
data = cursor.fetchall ()

for row in data :
	print "\n --- \n"
	print "domain: " + row[0] + "\n" + "active: " + str(ord(row[1])) + "\n" + "program: " + row[2] + "\n" + "scope: " + str(ord(row[1]))


cursor.close ()
connection.close ()
sys.exit()

