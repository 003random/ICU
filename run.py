#!/usr/bin/python
try:
	import sys, os, MySQLdb, datetime

	connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")
	cursor = connection.cursor ()

	cursor.execute ("insert into scans (StartDate) values (CURRENT_TIMESTAMP)")
	connection.commit()
	scanId = cursor.lastrowid
	cursor.execute ("select Domain from domains where TopDomainID is NULL order by Domain")
	data = cursor.fetchall ()
	connection.close()

	for row in data:
		print "Running sublister on " + row[0]
		os.system("python " + os.path.dirname(os.path.abspath(__file__))  + "/database/additional_tools/sublister_to_db.py " + row[0] + " " + str(scanId))

	connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")
	cursor = connection.cursor ()
	cursor.execute ("update scans set EndDate = CURRENT_TIMESTAMP where ScanID = %s", (scanId))
	connection.commit()
	connection.close()

	os.system("python " + os.path.dirname(os.path.abspath(__file__))  + "/telegram/notify.py " + str(scanId))
except Exception, e:
	print "error: " + str(e)
	with open(os.path.dirname(os.path.abspath(__file__))  + '/logs/run_logs.txt', 'w+') as the_file:
		the_file.write(str(e) + "\n")
