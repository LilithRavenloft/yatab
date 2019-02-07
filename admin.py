from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Message, Chat, Update, Bot, User
from telegram.error import BadRequest
import logging as log
from db_handler import db

db = db()

def pin(bot: Bot, update: Update):
    
    chat = update.effective_chat            #in what chat is the message supposed to be pinned?
    is_group = chat.type != "private" and chat.type != "channel"
    
    message = update.effective_message      #message to be pinned
    
    log.info("pin message {}".format(message.text))
    
    db.put("pins", message.text)
    
    is_silent = False
    if message and is_group:
        try:
            bot.pin_chat_message(chat.id, message.message_id, disable_notification=is_silent, timeout=None)
            log.info("pinned")
        except BadRequest as e:
            log.info("bad request: {}".format(e.message))
            pass
    return