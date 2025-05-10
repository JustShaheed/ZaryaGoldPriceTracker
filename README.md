# 📈 ZARYA Gold Price Tracker

A Python automation script that tracks live gold prices using [GoldAPI.io](https://www.goldapi.io/) and sends hourly updates to your Telegram bot.

## Features
- Real-time gold price in USD
- Hourly Telegram updates
- Secure config with `.env` file

## Setup
1. Create a `.env` file with:
API_KEY=your_goldapi_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id

2. Install dependencies:
pip install requests python-dotenv

3. Run the tracker:
tracker.py