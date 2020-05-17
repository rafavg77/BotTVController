#!/bin/bash

cd /opt/bots/BotTVController/
sudo git pull
sudo chmod +x run.sh
source BotTvController/bin/activate
python3.7 src/bot.py
