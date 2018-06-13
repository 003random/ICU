#!/usr/bin/env bash

echo "[+] Installing sublist3r"
git clone https://github.com/aboul3la/Sublist3r.git tools/dependencies/sublister

echo "----------------------------------------------------------------"

echo "[?] Do you want to pip install the requirements.txt?"
echo "[Y/n]"
read choice_pip_requirements

if [ "$choice_pip_requirements" == "Y" ] || [ "$choice_pip_requirements" == "y" ] || [ -z "$choice_pip_requirements" ]; then
        pip install -r requirements.txt
	sudo apt-get install python-mysqldb
else
	echo "[!] Make sure you have the right modules installed. You can check which modules are used in requirements.txt"
fi

echo "----------------------------------------------------------------"

echo "[?] What is the database username?"
read database_username

echo "[?] What is the database password?"
read database_password

echo "[?] What is the database server? e.g. localhost (most common), if it runs on the same server."
read database_server

echo "
database_username = \"$database_username\"
database_password = \"$database_password\"
database_server = \"$database_server\"
database_name = \"recon\"

telegram_bot_token = \"\"
telegram_chat_id = \"\"
" > "credentials.py"

echo "[+] Creating database 'recon' with tables 'domains', scans and 'errors'"
python database/init_db.py

echo "[+] Checking if the database was created successfully"
python database/db_test.py

echo "----------------------------------------------------------------"

echo "[+] Adding a cron task to run 'run.py' every 12 hours. You can edit this with the command 'crontab -e'"
echo "[?] Adding the path to crontab. If this isn't the right path to the file, please edit this with the command 'crontab -e'"
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 */12 * * * python $(pwd)/run.py" >> mycron
#install new cron file
crontab mycron
rm mycron
echo "[+] Crontab task created!"

echo "----------------------------------------------------------------"

echo "[?] Do you want to create ICU.php? A simple web interface for the domains."
echo "[Y/n]"
read choice_web

if [ "$choice_web" == "Y" ] || [ "$choice_web" == "y" ] || [ -z "$choice_web" ]; then
        ./web/setup.sh "$database_username" "$database_password" "$database_server"
	echo "[+] ICU.php was added."
fi

echo "----------------------------------------------------------------"

echo "[!] All set!"

echo "----------------------------------------------------------------"

echo "[+] If you want to use the telegram options, please add your telegram bot token in credentials.py."
echo "[?] Do you want to run main.py? This script lets you manage your domains."
echo "[Y/n]"
read choice_main

if [ $choice_main = "Y" ] || [ $choice_main = "y" ] || [ -z $choice_main ]; then
	python main.py
fi
