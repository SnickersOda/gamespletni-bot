import telebot

TOKEN = "8496720283:AAEjnICiSleU6iNu9pBrntpIHiuO9FonTls"
ADMIN_ID = 5459551688  # сюда вставь свой Telegram ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🔥 Предложка GameSpletni.\n\n"
        "Отправь новость, инсайд или мем.\n"
        "Админы всё проверят."
    )

@bot.message_handler(content_types=['text', 'photo', 'video', 'document'])
def forward_to_admin(message):
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "✅ Отправлено на рассмотрение.")

bot.infinity_polling()