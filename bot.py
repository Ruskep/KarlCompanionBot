import os
import telebot
import schedule
import time
import threading
from random import choice
from dotenv import load_dotenv

# Загрузка токенов из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TOKEN)

# Сообщения от "Карла"
RANDOM_MESSAGES = [
    "Привет! Это Карл Компаньон. Как твои дела? 🌟",
    "Эй, не хочешь обсудить последние новости из ПР?",
    "Я тут подумал... А как бы Дилан поступил в этой ситуации? 🤔"
]

# Функция авто-сообщений
def send_random_message():
    bot.send_message(CHAT_ID, choice(RANDOM_MESSAGES))

# Планировщик (каждые 3-8 часов)
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

schedule.every(3).to(8).hours.do(send_random_message)

# Обработчик команд
@bot.message_handler(func=lambda m: True)
def reply(message):
    response = f"🔹 Карл Компаньон: Я пока что учусь отвечать как DeepSeek, но скоро научусь! Ты написал: '{message.text}'"
    bot.reply_to(message, response)

# Запуск
if __name__ == "__main__":
    threading.Thread(target=run_scheduler, daemon=True).start()
    bot.polling(non_stop=True)
