#!/usr/bin/python

import MySQLdb
import sys

connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")

cursor = connection.cursor ()
cursor.execute ("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format("domains"))

if cursor.fetchone()[0] == 1:
        print "[+] Table domains found"
else:
	print "[-] Hmm... No table 'domains' was found in the database recon. Did you run the initialize script?"


cursor.execute ("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format("errors"))

if cursor.fetchone()[0] == 1:
        print "[+] Table errors found"
else:
        print "[-] Hmm... No table 'errors' was found in the database recon. Did you run the initialize script?"

cursor.execute ("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format("scans"))

if cursor.fetchone()[0] == 1:
        print "[+] Table scans found"
else:
        print "[-] Hmm... No table 'scans' was found in the database recon. Did you run the initialize script?"


cursor.close ()
connection.close ()
sys.exit()

