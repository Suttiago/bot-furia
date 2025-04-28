from scrappy.get_nextgames import get_games

def setup_message_nextgames(bot):
    @bot.message_handler(commands=['proximosjogos'])
    def message_nexgames(message):
        bot.reply_to(message, get_games)
