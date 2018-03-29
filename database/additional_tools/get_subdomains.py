#!/usr/bin/python
import os, sys, MySQLdb

connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")
domain = sys.argv[1].strip()
cursor = connection.cursor()

cursor.execute ("select Domain from domains where TopDomainID = (select DomainID from domains where Domain = %s)", (domain,))

data = cursor.fetchall()
#Get first the values out of tuple and create an array with them
database_domains = [d[0] for d in data]

for row in database_domains:
	print row

#cursor.execute("select DomainID from domains where Domain = %s", (domain,))
#data = cursor.fetchall()
#data = data[0][0]
#print "also the TopDomainId = " + str(data)

cursor.close ()
connection.close ()
sys.exit()
