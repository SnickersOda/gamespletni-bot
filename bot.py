import os
import telebot

TOKEN = os.getenv("TOKEN")
ADMIN_ID = 5459551688  # сюда вставь свой Telegram ID

bot = telebot.TeleBot(TOKEN)
