import os
import telebot
from pprint import pprint
bot = telepot.TeleBot(os.environ.get("BOT_TOKEN"))
pprint(bot.getMe())
pprint(bot.getUpdates())
#WEBHOOK_URL = "https://webhook.site/32bed6d3-b8db-42f0-83b2-6b441de5b178"