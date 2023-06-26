import telebot
from telebot import types

import config
from main import getPassword
import re

bot = telebot.TeleBot(config.API, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi")

@bot.message_handler(commands=['link'])
def sendPassword(message):

	if (message.reply_to_message == None):
		link = str(re.findall("(https?://\S+)", message.text)[0])
		bot.reply_to(message, getPassword(link))
	else:
		link = str(re.findall("(https?://\S+)", message.reply_to_message.text)[0])
		bot.reply_to(message, getPassword(link))


bot.infinity_polling()