#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TEL_KEY=os.environ['BOT_TEL_KEY']
BOT_NGR_KEY=os.environ['BOT_NGR_KEY']


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(BOT_TEL_KEY, use_context=True)

    logger.info("Bot encendido")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
   
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()

