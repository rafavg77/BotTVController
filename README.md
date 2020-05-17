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
sudo python3.7 -m venv BotTvController
source BotTvController/bin/activate
sudo pip3 install -U -r requirements.txt
sudo chmod +x run.sh
./run.sh
sudo cp /opt/bots/BotTVController/services/bot-tvcontroller.service /lib/systemd/system/
sudo systemctl enable bot-tvcontroller.service
sudo service bot-tvcontroller status
sudo service bot-tvcontroller start
sudo service bot-tvcontroller status
```
