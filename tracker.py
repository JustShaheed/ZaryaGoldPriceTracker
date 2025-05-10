import requests
import time
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
UPDATE_INTERVAL = 3600  # in seconds

def get_gold_price():
    url = 'https://www.goldapi.io/api/XAU/USD'
    headers = {
        'x-access-token': API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    if 'price' in data:
        return data['price']
    else:
        raise Exception(f"API error: {data}")

def send_telegram_message(message):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(telegram_url, data=payload)

while True:
    try:
        gold_price = get_gold_price()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"📢 Gold Price Update\n\n🕒 {timestamp}\n💰 Price: {gold_price:.2f} USD/oz"
        print(message)
        send_telegram_message(message)
    except Exception as e:
        print(f"[ERROR] {e}")
    time.sleep(UPDATE_INTERVAL)
