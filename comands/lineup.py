from utils.messages import Lineup

def setup_message_line(bot):
    @bot.message_handler(commands=['lineup'])
    def message_lineup(message):
        bot.reply_to(message, Lineup)