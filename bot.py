import os
import telebot


TOKEN = os.getenv("TELEGRAM_TOKEN")
ADMIN_ID = 5459551688

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Предложка GameSpletni.\n\nОтправь новость, инсайд или мем.\nАдмины всё проверят."
    )


@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    
    bot.send_message(
        ADMIN_ID,
        f"От @{message.from_user.username} (ID: {message.from_user.id}):\n{message.text}"
    )

    bot.send_message(message.chat.id, "✅ Спасибо! Твоё сообщение отправлено админам.")


bot.infinity_polling(timeout=10, long_polling_timeout=5)
