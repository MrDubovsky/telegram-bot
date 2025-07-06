import os
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

bot = TeleBot(BOT_TOKEN)

# Обработчик команды /start: приветственное сообщение пользователю
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Напиши сюда всё, что считаешь нужным. Если хочешь, чтобы мы опубликовали это, напиши в сообщении об этом."
    )

# Приём любых личных сообщений от пользователей (кроме команд) и пересылка администратору
@bot.message_handler(func=lambda m: m.chat.type == 'private' and m.from_user.id != ADMIN_ID and not m.text.startswith('/'))
def handle_user_msg(message):
    # Пересылаем сообщение администратору
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    # Подтверждаем пользователю
    bot.reply_to(message, "Спасибо! Ваше сообщение отправлено на рассмотрение.")

if __name__ == '__main__':
    print("Bot started...")
    bot.infinity_polling()
