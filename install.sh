 #!/usr/bin/env bash

# Install sublis3r
#git clone https://github.com/aboul3la/Sublist3r.git tools/dependencies/sublister

#echo "- Creating database 'recon' with tables 'domains' and 'errors' -"
#python database/init_db.py

#echo "- Checking if the database was created successfully -"
#python database/db_test.py

echo "- Adding a cron task to run 'run.py' every 12 hours. You can edit this with the command 'crontab -e' -"
echo "Check?: Adding the path to crontab. If this isn't the right path to the file, please edit this with the command 'crontab -e'"
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 */12 * * * python $(pwd)/run.py" >> mycron
#install new cron file
crontab mycron
rm mycron
