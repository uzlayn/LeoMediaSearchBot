import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'BQC6kfsAVd4ZkiWtMz_lW9BZNEYD_jfxtBTPSsnrZcywz6TZFr4WhbSLpkeULtwhR4jYwNoQ_HazMpPD3TNM-AZOX9KeexKPQfZMtd_oL-GPOx8TW0E3prFAYgNm6bXoxTgsQufE0vK7ASFdzDqhf9jF8asnR97m339DzcOlQwXBUqc-BpLWHYhNuipD32jTv5eTfD3ie6zvG7oqQmkLsvP5oAspNbrwXn9oFvzNrrJtZyCpZvaNDFUPWHifpbCkXiLbqxnoOusN7RInRfGnAbxM9e8W7qRvtA7dpJqTBLHYSlkxMGp36r0qG1e6aDGxLz0dsTQbF5AuCdy9KS7qhWAqS9I8nQAAAAFa5ESRAA')
USER_SESSION = environ.get('BQC6kfsAVd4ZkiWtMz_lW9BZNEYD_jfxtBTPSsnrZcywz6TZFr4WhbSLpkeULtwhR4jYwNoQ_HazMpPD3TNM-AZOX9KeexKPQfZMtd_oL-GPOx8TW0E3prFAYgNm6bXoxTgsQufE0vK7ASFdzDqhf9jF8asnR97m339DzcOlQwXBUqc-BpLWHYhNuipD32jTv5eTfD3ie6zvG7oqQmkLsvP5oAspNbrwXn9oFvzNrrJtZyCpZvaNDFUPWHifpbCkXiLbqxnoOusN7RInRfGnAbxM9e8W7qRvtA7dpJqTBLHYSlkxMGp36r0qG1e6aDGxLz0dsTQbF5AuCdy9KS7qhWAqS9I8nQAAAAFa5ESRAA', 'Uzlaynbot')
APP_ID = int(environ['25336929'])
API_HASH = environ['308f4c34a6c3b90a74546d7e7e3087c2']
BOT_TOKEN = environ['6705541825:AAGVNZE9qUtTVyfMe0_m4aL06L1EGHjLli8']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')
BOT_OWNER = int(os.environ.get("5819876497")
BOT_USERNAME = os.environ.get("Uzlaynbot")

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 15))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

# MongoDB information
DATABASE_URI = environ['mongodb+srv://vaqtm:vaqtm@cluster0.a3burak.mongodb.net/?retryWrites=true&w=majority']
DATABASE_NAME = environ['inline']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "flase"))
UPDATES_CHANNEL = os.environ.get("-1002089478560")

#ban/unban
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))

#for broadcast and user stts db
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://vaqtm:p1uP6mprrpV4WKHA@cluster0.gaydlw5.mongodb.net/?retryWrites=true&w=majority")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoMediaSearchBot")
# Messages
default_start_massege = """
**Hi {}👋

I'm Media Search Bot**

You can start searching by the "Search Media 🔎" button below 😊
"""

default_share_button_text = """
Media Search Bot 🇱🇰

Here you can find any media file by searching its name 😊

Bot : {username} 🤖 🇱🇰
Updates Channel: @uzlaynuz 🇱🇰
Developper : @Mdddyou 🇱🇰
"""

START_MSG = environ.get('START_MSG', default_start_massege)

SHARE_BUTTON_TEXT = environ.get('SHARE_BUTTON_TEXT', default_share_button_text)

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @uzlaynuz to use this bot')
