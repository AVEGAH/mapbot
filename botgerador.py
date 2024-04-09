#!/usr/bin/env python3

import random
import string
import telegram
from telegram.ext import Updater, CommandHandler

# Telegram bot token obtained from BotFather
TOKEN = '6760890328:AAFTyhR88Uf9pePTS3qemqQYDrvnNOR_oMk'

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Command handler for /password command
def password(update, context):
    length = int(context.args[0]) if context.args else 12
    password = generate_password(length)
    update.message.reply_text(f"Generated password: {password}")

def main():
    # Create the bot updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command handlers
    dp.add_handler(CommandHandler("password", password, pass_args=True))

    #
