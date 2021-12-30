
import telebot
from bs4 import BeautifulSoup
import os
import requests

url = "https://www.tgju.org/profile/sekeb"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
token = os.environ['5057221416:AAEPGZWbmS0v2zTcRVJzs9vxIt-wsBwkFvg']

for web in soup.find_all(class_='price',limit=1):
  
    havij = BeautifulSoup(web.text, "html.parser")
API_TOKEN = "5057221416:AAEPGZWbmS0v2zTcRVJzs9vxIt-wsBwkFvg"

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start','seke'])

@bot.message_handler(func=lambda message: True)
def seke(message):
    bot.reply_to(message, havij.text)


bot.infinity_polling()
