#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telegram, sys, os, logging, datetime
from telegram import (InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton)
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
import credentials

telegram_bot_token = credentials.telegram_bot_token


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
	user = update.message.from_user
	chat_id = str(update.message.chat_id)

	with open(os.path.dirname(os.path.abspath(__file__)) + "/../credentials.py") as f:
		var_lines = f.readlines()
		var_lines = [x.strip() for x in var_lines]
	f.close()

	new_lines = []

	for line in var_lines:
		if line.startswith("telegram_chat_id"):
			new_lines.append("telegram_chat_id = \"" + str(chat_id) + "\"")
		else:
			new_lines.append(line)

	creds = open(os.path.dirname(os.path.abspath(__file__)) + "/../credentials.py", 'w')
	for item in new_lines:
		if item:
			creds.write("%s\n" % item)
	creds.close()
	update.message.reply_text("Welcome " + str(user['first_name']) + "! The telegram setup is successfully finished.")
	print "Success! You can now close the setup with ctr + c"
	return ConversationHandler.END

def main():
	updater = Updater(telegram_bot_token)
	dp = updater.dispatcher

	print "[!] Send /start to the bot."

	conv_handler = ConversationHandler(
		entry_points=[CommandHandler('start', start)],

		states={
		},

		fallbacks=[CommandHandler('cancel', cancel)]
	)

	dp.add_handler(conv_handler)
	updater.start_polling()
	updater.idle()

def cancel(bot, update):
	print "canceled"
	return ConversationHandler.END

if __name__ == '__main__':
	main()
