#!/usr/bin/python

import sys, datetime, MySQLdb, telegram, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import credentials

if credentials.telegram_bot_token == "" or credentials.telegram_chat_id == "":
	print "[+] No telegram bot token and/or telegram chat id set in credentials.py"
	sys.exit()

bot = telegram.Bot(credentials.telegram_bot_token)
scanId = sys.argv[1]
message = "*" + str(datetime.datetime.now().replace(microsecond=0)) + "*"

connection = MySQLdb.connect (host = credentials.database_server, user = credentials.database_username, passwd = credentials.database_password, db = credentials.database_name)
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

bot.send_message(chat_id=credentials.telegram_chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
