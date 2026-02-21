import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = 5459551688  # сюда вставь свой Telegram ID

bot = telebot.TeleBot(TOKEN)
bot.polling(none_stop=True)

