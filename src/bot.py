#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
from catt.api import CattDevice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TEL_KEY=os.environ['BOT_TEL_KEY']
BOT_NGR_KEY=os.environ['BOT_NGR_KEY']


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
	cast = CattDevice(name="TV Recamara")
	VIDEOS = [ "https://www.youtube.com/watch?v=nUwEVoLB-tA" ]
	for video in VIDEOS:
		 cast.play_url(video, resolve=True, block=True)
	update.message.reply_text('Video enviado')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(BOT_TEL_KEY, use_context=True)

    logger.info("Bot encendido")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("cast", cast))
   
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

