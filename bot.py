import os
from telebot import TeleBot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

bot = TeleBot(BOT_TOKEN)

# Приём личных сообщений от пользователей и пересылка администратору
@bot.message_handler(func=lambda m: m.chat.type == 'private' and m.from_user.id != ADMIN_ID)
def handle_user_msg(message):
    # Пересылаем сообщение вам
    bot.forward_message(ADMIN_ID, message.chat.id, message.message_id)
    # Подтверждаем пользователю
    bot.reply_to(message, "Спасибо! Ваше сообщение отправлено на рассмотрение.")

if __name__ == '__main__':
    print("Bot started...")
    bot.infinity_polling()
