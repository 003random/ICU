#!/usr/bin/python
import os, sys, MySQLdb, time
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../../")
import credentials

try:
	domain = sys.argv[1].strip()
	scanId = sys.argv[2]

	if not os.path.exists("/tmp/ICU"):
		os.makedirs("/tmp/ICU")

	if not os.path.exists("/tmp/ICU/"+domain+"/"):
	    os.makedirs("/tmp/ICU/"+domain+"/")

	#Add new subdomain scanners here. Make sure to let them save the output to /tmp/ICU/{domain}/doains-all.txt
	os.system(os.path.dirname(os.path.abspath(__file__)) + "/../../tools/dependencies/sublister/sublist3r.py -o /tmp/ICU/"+domain+"/domains-all.txt -d "+domain)
	time.sleep(2)

	try:
		#Subfinder
		os.system("subfinder -d " + domain + " -v -o /tmp/ICU/"+domain+"/domains-subfinder.txt --timeout 6")
		time.sleep(2)

		#Amass
		os.system("amass -o /tmp/ICU/"+domain+"/domains-amass.txt -d " + domain)
        	time.sleep(2)
	except Exception as e:
		print "An error occured; You probably dont have either subfinder or amass installed. Check the README.md to see you how to install them. Error: "
		print str(e)


	connection = MySQLdb.connect (host = credentials.database_server, user = credentials.database_username, passwd = credentials.database_password, db = credentials.database_name)
	cursor = connection.cursor()

	#Retrieve all info from a top domain and its subdomains, so we can use this data instead of opening new db connections later on
	cursor.execute("select Domain, TopDomainID, Active, Program, DomainID, scan_Id from domains where TopDomainID = (select DomainID from domains where Domain = %s) or Domain = %s", (domain, domain))
	database_data = cursor.fetchall()
	database_domains = [d[0] for d in database_data]

        non_active_subdomains = [x[0] for x in database_data if ord(x[2]) == False]
        program = [x[3] for x in database_data if x[0] == domain][0]
        topDomainID = [x[4] for x in database_data if x[0] == domain][0]

	#All the domains from the subdomain scanners
	domains_all = open("/tmp/ICU/"+domain+"/domains-all.txt",'r').read().split('\n')

	try:
		#Domains from subfinder
		domains_subfinder = open("/tmp/ICU/"+domain+"/domains-subfinder.txt",'r').read().split('\n')

	        #Domains from amass
        	domains_amass = open("/tmp/ICU/"+domain+"/domains-amass.txt",'r').read().split('\n')

	        #Add the subfinder domains
        	domains_all.extend(x for x in domains_subfinder if x not in domains_all)

		#unique
		domains_all = list(set(domains_all))

	        #Add the amass domains
        	domains_all.extend(x for x in domains_amass if x not in domains_all)

        	#unique
        	domains_all = list(set(domains_all))
        except Exception as e:
                print "An error occured; You probably dont have either subfinder or amass installed. Check the README.md to see you how to install them. Error: "
                print str(e)

	#Add all the database subdomain to it
	domains_all.extend(x for x in database_domains if x not in domains_all)

	#unique -- Unique each time after adding a new list, to limit ram usage
	domains_all = list(set(domains_all))

	#Put all the online domains in a domains-online.txt
	os.system(os.path.dirname(os.path.abspath(__file__)) + "/../../tools/online.py /tmp/ICU/"+domain+"/domains-all.txt /tmp/ICU/"+domain+"/domains-online.txt")

	#Convert online domains to array
	domains_online = open("/tmp/ICU/"+domain+"/domains-online.txt",'r').read().split('\n')

	#Loop through every subdomain
	for sub_domain in domains_all:
		#Get the scanID to insert. If the domains was already in the db and isnt changed, then keep the old scanID. otherwise use the scanID of the current scan
	        insertScanId = scanId if not [x[5] for x in database_data if x[0] == sub_domain] else [x[5] for x in database_data if x[0] == sub_domain][0]

		#If the subdomain is online
		if sub_domain in domains_online:
			active=True
			#If the subdomain used to be offline, give it the current scanID
			if sub_domain in non_active_subdomains:
				insertScanId = scanId
		else:
			active=False


		if sub_domain:
			#Insert the new values, or update them if they already existed
			cursor.execute("INSERT INTO domains (Program, TopDomainID, Active, InScope, Domain, scan_Id) VALUES (%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Active = %s, LastModified = now(), scan_Id = %s", (program, topDomainID, active, 1, sub_domain, insertScanId, active, insertScanId))
			connection.commit()

	cursor.close ()
	connection.close ()
except Exception as e:
	#Handle the errors, and save them to the database
	print "error in domains_db.py with main domain; " + domain
	cursor.execute("INSERT INTO errors (Domain, ErrorDescription, Error, Script, scan_Id) VALUES (%s, %s, %s, %s, %s) ", (domain, "error in domains_db.py with main domain; "+domain, e, "sublister_to_db.py", scanId))
	connection.commit()
	cursor.close()
	connection.close()
	print e
sys.exit()
