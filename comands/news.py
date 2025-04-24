from utils.messages import Noticias

def setup_message_news(bot):
    @bot.message_handler(commands=['news'])
    def message_news(message):
        bot.reply_to(message, Noticias)
