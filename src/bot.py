#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import logging
import requests
import schedule
import time
import subprocess
from threading import Timer 
from catt.api import CattDevice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

parser = ConfigParser()
parser.read('config/auth')

BOT_TEL_KEY=os.environ['BOT_TEL_KEY']
#BOT_NGR_KEY=os.environ['BOT_NGR_KEY']
CAST_DEVICE="TV Recamara"
CHAT_ID="32268671"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    username = update.message.chat.username
    update.message.reply_text('Hi master %s,  I\'m here to serve you!' % (username))
    logger.info("Command /start from %s" % (username))

def help(update, context):
    username = update.message.chat.username
    update.message.reply_text('Este el comando de ayuda')
    logger.info("Command /help from %s" % (username))

def cast(update, context):
	update.message.reply_text('Enviando video')
	cast = CattDevice(name=CAST_DEVICE)
	VIDEOS = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', update.message.text)
	logger.info(VIDEOS)
	for video in VIDEOS:
		 cast.play_url(video, resolve=True, block=True)
	update.message.reply_text('Video enviado')

def pause(update, context):
	cast = CattDevice(name=CAST_DEVICE)
	cast.pause()
	update.message.reply_text('Comando Pause enviado')

def status():
	sendMessage("Sigo Vivo")
	Timer(60,status).start()

def sendMessage(message):
	bot_token = BOT_TEL_KEY
	bot_chatID = CHAT_ID
	bot_message = message
	send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
	response = requests.get(send_text)
	print(response.json())

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

#status()

#def job():
#	p = subprocess.Popen("catt scan | grep -v \"Scanning Chromecasts...\"", stdout=subprocess.PIPE, shell=True)
#	(output, err) = p.communicate()
#	print ("Command output : ", output)
#	sendMessage(str(output, 'utf-8'))

#schedule.every(1).minutes.do(job)

def main():
    updater = Updater(BOT_TEL_KEY, use_context=True)

    logger.info("Bot encendido")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("cast", cast))
    dp.add_handler(CommandHandler("pause", pause))
   
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

#while True:
#    schedule.run_pending()
#    time.sleep(1)

if __name__ == '__main__':
    main()