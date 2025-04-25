import os
import time
import configparser
import subprocess
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# خواندن تنظیمات از فایل config.ini
config = configparser.ConfigParser()
config.read('config.ini')

BOT_TOKEN = config['bot']['token']
ADMIN_ID = int(config['bot']['admin_id'])
SERVER_IP = config['server']['ip']
SERVER_PASSWORD = config['server']['password']
START_PORT = int(config['server']['start_port'])
END_PORT = int(config['server']['end_port'])
CURRENT_PORT = START_PORT

active_proxies = {}

def is_admin(update: Update):
    return update.effective_user.id == ADMIN_ID

[... بقیه کدها مانند قبل ...]

if __name__ == '__main__':
    print("🔥 راه‌اندازی ربات MTProto-Star")
    print(f"👤 مدیر ربات: {ADMIN_ID}")
    print(f"🌐 سرور: {SERVER_IP}")
    print(f"🔌 محدوده پورت: {START_PORT}-{END_PORT}")
    main()
