from utils.messages import Help

def setup_message_help(bot):
    @bot.message_handler(commands=['help'])
    def message_help(message):
        bot.reply_to(message, Help)