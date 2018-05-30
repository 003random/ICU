#!/usr/bin/python
import MySQLdb
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import credentials

connection = MySQLdb.connect (host = credentials.database_server, user = credentials.database_username, passwd = credentials.database_password, db = credentials.database_name)

cursor = connection.cursor ()
cursor.execute ("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format("domains"))

if cursor.fetchone()[0] == 1:
        print "    [+] Table domains found"
else:
	print "    [-] Hmm... No table 'domains' was found in the database recon. Did you run the initialize script?"


cursor.execute ("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format("errors"))

if cursor.fetchone()[0] == 1:
        print "    [+] Table errors found"
else:
        print "    [-] Hmm... No table 'errors' was found in the database recon. Did you run the initialize script?"

cursor.execute ("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format("scans"))

if cursor.fetchone()[0] == 1:
        print "    [+] Table scans found"
else:
        print "    [-] Hmm... No table 'scans' was found in the database recon. Did you run the initialize script?"


cursor.close ()
connection.close ()
sys.exit()

