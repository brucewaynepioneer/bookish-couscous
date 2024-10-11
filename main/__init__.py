from telethon.errors import FloodWaitError
from datetime import datetime as dt, timedelta
import asyncio
import sys
from pyrogram import Client
import uvloop
from pyrogram.errors import FloodWait
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from decouple import config
import logging, time

# Setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# Use uvloop for better performance
uvloop.install()

# Load sensitive variables from the .env file
MONGODB = config("MONGODB_CONNECTION_STRING", default="None")
API_ID = config("API_ID", cast=int)  # Ensure API_ID is cast to an integer
API_HASH = config("API_HASH")
BOT_TOKEN = config("BOT_TOKEN")
SESSION = config("SESSION")
FORCESUB = config("FORCESUB")
AUTH = config("AUTH")
OWNER_ID = int(config("OWNER_ID", default="7410008859"))  # Fallback value if OWNER_ID not set
LOG_GROUP = int(config("LOG_GROUP", default="1002232767054"))

# Convert AUTH to a set of integers for SUDO_USERS
SUDO_USERS = set(map(int, AUTH.split())) if AUTH else set()

# Initialize the bots
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
userbot = Client("myacc", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re-add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "ggnbot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    sys.exit(1)
