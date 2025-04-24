from utils.messages import Start

def setup_message_start(bot):
    @bot.message_handler(commands=['start'])
    def message_start(message):
        bot.reply_to(message, Start)