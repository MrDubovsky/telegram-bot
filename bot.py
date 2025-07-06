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

if __name__ == '__main__':
    print("Bot started...")
    bot.infinity_polling()
