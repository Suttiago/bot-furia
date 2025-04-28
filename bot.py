import telebot
import os
from dotenv import load_dotenv
from comands.start import setup_message_start
from comands.help import setup_message_help
from comands.lineup import setup_message_line
from comands.quiz import setup_message_quiz
from comands.news import setup_message_news
from comands.lastgames import setup_message_lastgames
from comands.nextgames import setup_message_nextgames

load_dotenv()

token = os.getenv("token")
bot = telebot.TeleBot(token)

setup_message_start(bot)
setup_message_help(bot)
setup_message_line(bot)
setup_message_quiz(bot)
setup_message_news(bot)
setup_message_lastgames(bot)
setup_message_nextgames(bot)

print("Bot está rodando...")
bot.infinity_polling()