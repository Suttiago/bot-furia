import telebot
from dotenv import load_dotenv
import os
from comands.start import setup_message_start
from comands.help import setup_message_help
from comands.lineup import setup_message_line
from comands.quiz import setup_message_quiz


load_dotenv()


token = os.getenv("token")

bot = telebot.TeleBot(token)


setup_message_start(bot)
setup_message_help(bot)
setup_message_line(bot)
setup_message_quiz(bot)



print("Bot está rodando...")
bot.infinity_polling()