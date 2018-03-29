#!/usr/bin/python

import sys, datetime, MySQLdb, telegram

bot = telegram.Bot('576071746:AAH2TYv_IDgh4r-bAnO9yE0LioSewbDuVPI')
scanId = sys.argv[1]
message = "*" + str(datetime.datetime.now().replace(microsecond=0)) + "*"

connection = MySQLdb.connect (host = "localhost", user = "rjp", passwd = "1484", db = "recon")
cursor = connection.cursor()

cursor.execute ("select * from domains where scan_Id = %s and Active order by TopDomainID", (scanId))
newSubDomains = cursor.fetchall()

cursor.execute ("select * from errors where scan_Id = %s order by ErrorDate", (scanId))
errors = cursor.fetchall()

connection.close()

message += "\n_Scan " + str(scanId) + "_"

message += "\n"

if len(errors) > 1:
        message += "\n(" + str(len(errors)) + "  Errors)"
elif len(errors) == 1:
        message += "\n(" + str(len(errors)) + "  Error)"

if len(errors) > 0:
	message += "\n--------------"

if len(newSubDomains) > 1:
	message += "\n\[+] " + str(len(newSubDomains)) + " New subdomains:"
elif len(newSubDomains) == 1:
	message += "\n\[+] " + str(len(newSubDomains)) + " New subdomain:"

message += ""

bot.send_message(chat_id=476443218, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
