## 📌 Description

# Install
```bash ./install.sh ``` The installation script asks for various things, including your MySQL database username and password. These will be saved in credentials.py. You can always 
change these credentials later on.

# Telegram
ICU also includes a telegram bot and notifications part. If you want to use this, you will have to include your telegram bot token in credentials.py. You can get a telegram bot 
token [here]("https://core.telegram.org/bots#3-how-do-i-create-a-bot"). Next off, you need to run setup.py in /telegram, and then send /start to the bot. This will save your chat_id 
to credentials.py so it can be used for authentication with the bot, and to send the notifications to.

# Modules
The following modules are used: MySQLdb, telegram, random, sys, os, datetime, logging, time.
 
the install script offers an option to install the modules from requirements.txt. This requires pip to be installed. If, for some reason, some modules are still missing. Then 
install these modules. The most important one is MySQLdb. [here]("https://stackoverflow.com/questions/25865270/how-to-install-python-mysqldb-module-using-pip") you can read how to 
install MySQLdb.

# Extra
To get ICU up and running, requires some simple skills. 👌 *Created by [003random](http://hackerone.com/003random) - [@003random](https://twitter.com/rub003) - 
[003random.com](https://poc-server.com/blog/)*
