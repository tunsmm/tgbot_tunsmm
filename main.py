import os

import telegram
from dotenv import load_dotenv 

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)

def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)

send_message('Hello world!')
