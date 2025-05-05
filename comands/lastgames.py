from scrappy.get_lastgames import get_last_games

def setup_message_lastgames(bot):
    @bot.message_handler(commands=['ultimosjogos'])
    def message_news(message):
        bot.reply_to(message, get_last_games())
