from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from admin import pin
import logging
updater = Updater(token='701820948:AAGQHguPM1Wk20_gnEkZZjRuisJQFo3Reyc')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

log = logging.getLogger(__name__)

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Huhu, ich bin ein alpakadministrator!')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    log.warning('Update "%s" caused error "%s"', update, error)

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def main():
    """main"""
    #get the dispatcher for adding handlers
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("pin", pin))
    
    #log errors
    dispatcher.add_error_handler(error)
    
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)
    
    #let's start the bot
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()