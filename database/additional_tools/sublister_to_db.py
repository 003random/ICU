#!/usr/bin/python
import os, sys, MySQLdb

try:
	connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")
	domain = sys.argv[1].strip()
	cursor = connection.cursor()
	scanId = sys.argv[2]

	if not os.path.exists("/tmp/recon_domain_files"):
		os.makedirs("/tmp/recon_domain_files")

	if not os.path.exists("/tmp/recon_domain_files/"+domain+"/"):
	    os.makedirs("/tmp/recon_domain_files/"+domain+"/")

	os.system(os.path.dirname(os.path.abspath(__file__)) + "/../../../dependencies/sublister/sublist3r.py -o /tmp/recon_domain_files/"+domain+"/domains-all.txt -d "+domain)

	cursor.execute("select Domain, TopDomainID, Active, Program, DomainID, scan_Id from domains where TopDomainID = (select DomainID from domains where Domain = %s) or Domain = %s", (domain, domain))
	database_data = cursor.fetchall()
	database_domains = [d[0] for d in database_data]

        non_active_subdomains = [x[0] for x in database_data if ord(x[2]) == False]
        program = [x[3] for x in database_data if x[0] == domain][0]
        topDomainID = [x[4] for x in database_data if x[0] == domain][0]

	domains_all = open("/tmp/recon_domain_files/"+domain+"/domains-all.txt",'r').read().split('\n')
	domains_all.extend(x for x in database_domains if x not in domains_all)

	os.system(os.path.dirname(os.path.abspath(__file__)) + "/../../../tools/online.py /tmp/recon_domain_files/"+domain+"/domains-all.txt /tmp/recon_domain_files/"+domain+"/domains-online.txt")

	domains_online = open("/tmp/recon_domain_files/"+domain+"/domains-online.txt",'r').read().split('\n')

	for sub_domain in domains_all:
	        insertScanId = scanId if not [x[5] for x in database_data if x[0] == sub_domain] else [x[5] for x in database_data if x[0] == sub_domain][0]
		if sub_domain in domains_online:
			active=True
			if sub_domain in non_active_subdomains:
				insertScanId = scanId
		else:
			active=False

		if sub_domain:
			cursor.execute("INSERT INTO domains (Program, TopDomainID, Active, InScope, Domain, scan_Id) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Active = %s, LastModified = now(), scan_Id = %s", (program, topDomainID, active, 1, sub_domain, insertScanId, active, insertScanId))
			connection.commit()


	cursor.close ()
	connection.close ()
except Exception as e:
	print "error in sublister_to_db.py with main domain; " + domain
	cursor.execute("INSERT INTO errors (Domain, ErrorDescription, Error, Script, scan_Id) VALUES (%s, %s, %s, %s, %s) ", (domain, "error in sublister_to_db.py with main domain; "+domain, e, "sublister_to_db.py", scanId))
	connection.commit()
	cursor.close()
	connection.close()
	print e
sys.exit()
