# BotTVController
Bot de Telegram para enviar videos de Youtube y Facebook a un Chromecast

# Instrucciones
1. Configurar Variables de ambiente
2. Instalar requriments de python
3. Configurar ngrok
4. Configurar Bot como Servicio
5. Configurar Ngrok como Servicio
6. Ejecutar Bot

```bash 
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip python3-venv git
#add this to .bashrc
#export BOT_TEL_KEY=""
#export BOT_NGR_KEY=""
sudo mkdir /opt/bots/
cd /opt/bots/
sudo git clone https://github.com/rafavg77/BotTVController.git
cd BotTVController
sudo python3 -m venv BotTvController
source BotTvController/bin/activate
pip3 install -U -r requirements.txt
python3.7 src/bot.py
```
