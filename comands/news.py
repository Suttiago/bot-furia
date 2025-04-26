from scrappy.get_notices import get_notices

def setup_message_news(bot):
    @bot.message_handler(commands=['noticias'])
    def message_news(message):
        bot.reply_to(message, get_notices())
