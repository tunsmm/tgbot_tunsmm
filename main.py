import random
import os
import time

import telegram
from dotenv import load_dotenv 

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

bot = telegram.Bot(token=TELEGRAM_TOKEN)

messages = [
    "Hello, Boy!",
    "What's up, man?",
    "How's your doing?",
    "Hi, sweety..."
]

message_stats = {}

def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)


def choose_message(list_messages):
    return random.choice(list_messages)


def generate_message():
    choosing_message = choose_message(messages)
    
    # Stats
    if choosing_message in message_stats:
        message_stats[choosing_message] += 1
    else: 
        message_stats[choosing_message] = 1
    
    message = f"New message: {choosing_message}\n\n Stats: {message_stats}"
    return message


def main():
    while True:
        try:
            if True:
                message = generate_message()
                send_message(message)
            time.sleep(10)

        except Exception as e:
            print(f'Бот упал с ошибкой: {e}')
            time.sleep(10)
            continue


if __name__ == '__main__':
    main()
