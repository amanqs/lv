import os
from telethon import TelegramClient
import logging
from telegram.ext import Updater, CommandHandler, Dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO)
    
LOGGER = logging.getLogger(__name__)

class Config(object):
    LOGGER = True
    # Get this value from my.telegram.org! Please do not steal
    API_ID = int(os.environ.get("API_ID", 24322560))
    API_HASH = os.environ.get("API_HASH", "2dfcd3129785840826d235f7d160d82c")
    TOKEN = os.environ.get("TOKEN", "5995535272:AAHVX55wTF8xE66o1UnLthzEaxvi0q2qySc")
    SUDO_USERS = SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "2073506739").split())
    CHAT_ID = os.environ.get("CHAT_ID", "-1001753711304")
    DB_URI = os.environ.get("DATABASE_URL", "postgres://uoonwndo:Y-bNWoG1_ElhmGUu__sAhILP4dCUXdyh@babar.db.elephantsql.com/uoonwndo")
class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True

bot = TelegramClient('for', Config.API_ID, Config.API_HASH).start(bot_token=Config.TOKEN)
updater = Updater(Config.TOKEN, use_context=True)
dispatcher = updater.dispatcher
