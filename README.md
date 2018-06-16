## 📌 Description 
ICU is a tool to constantly keep an updated database of domains and subdomains, by regularly scanning domains for subdomains with the most common subdomain scanners.  
  
ICU works by creating a database with domains and a crontask to launch the subdomain scanners script. You can launch this script manually as well. You can also keep control of your domains and subdomains with the main.py script or with the telegram bot. There is also a simple web application that is meant for a quick view of your domains. This web application is not meant yet for a large number of domains.  
  
    
# Install 
```
git clone https://github.com/003random/ICU  
cd ICU
./install.sh 
```  
The installation script asks for various things, including your MySQL database username and password. These will be saved in credentials.py. You can always change these credentials later on. 

## Optional (recommended)
ICU also uses [Subfinder]("https://github.com/Ice3man543/subfinder") and [Amass]("https://github.com/caffix/amass/"). 
You need to install those as well. You need to have GO for those tools. [Here]("https://www.digitalocean.com/community/tutorials/how-to-install-go-on-debian-8") you can find how to install GO. 
After you've installed GO; Execute the following commands to install Amass and Subfinder: 
```
go get github.com/caffix/amass
go get github.com/Ice3man543/subfinder
```
 
 ## Setting up the MySql server

```

$sudo mysql_secure_installation

Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No: n

Remove anonymous users? (Press y|Y for Yes, any other key for No) : y

Success.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : y

Success.

Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y

 - Dropping test database...

Success.

 - Removing privileges on test database...

Success.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y

Success.

All done!

```
  
# Telegram 
ICU also includes a telegram bot and notifications part. If you want to use this, you will have to include your telegram bot token in credentials.py. You can get a telegram bot token [here]("https://core.telegram.org/bots#3-how-do-i-create-a-bot"). Next off, you need to run setup.py in /telegram, and then send /start to the bot. This will save your chat_id to credentials.py so it can be used for authentication with the bot, and to send the notifications to.  
   
# Modules 
The following modules are used: MySQLdb, telegram, random, sys, os, datetime, logging, time. 
 
The install script offers an option to install the modules from requirements.txt. This requires pip to be installed. If, for some reason, some modules are still missing. Then install these modules. The most important one is MySQLdb. [here]("https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip") you can read how to install MySQLdb.  

# Extra
To get ICU up and running, requires some simple skills. If you need serious help, you can contact me via twitter.  
 
# Credits 
Credits to:  
[Subfinder]("https://github.com/Ice3man543/subfinder"), [Amass]("https://github.com/caffix/amass/"), [Sublist3r]("https://github.com/aboul3la/Sublist3r")!

# Images  
![main.py](https://poc-server.com/github/ICU/main.py.png)
  ___  
![Telegram Bot](https://poc-server.com/github/ICU/telegrambot.png)

 
*Created by [003random](http://hackerone.com/003random) - [@003random](https://twitter.com/rub003) - [003random.com](https://poc-server.com/blog/)*  



