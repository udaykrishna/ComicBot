from xkcd_scraper import xkcd_grab
Api_Key="371007353:AAFKG29_gD1UjVl6aeeTe8NquIm8f9g_mVs"

from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler,Filters
from telegram import ChatAction,ReplyKeyboardMarkup


updater=Updater(token=Api_Key)
dispatcher=updater.dispatcher
xkcd=xkcd_grab()


custom_keyboard=[['Another Random Strip']]
reply_markup=ReplyKeyboardMarkup(custom_keyboard)

def start(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    bot.send_photo(chat_id=update.message.chat_id,photo=xkcd.get_random(),reply_markup=reply_markup)

def message(bot,update):
    if update.message.text == custom_keyboard[0][0]:
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        bot.send_photo(chat_id=update.message.chat_id,photo=xkcd.get_random(),reply_markup=reply_markup)
    else:
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        pic=xkcd.get_random()
        bot.send_message(chat_id=update.message.chat_id,text="I no understand what you say, but here's a comic strip :)")
        bot.send_photo(chat_id=update.message.chat_id,photo=pic,reply_markup=reply_markup)

start_handler=CommandHandler('start',start)
message_handler=MessageHandler(Filters.text,message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
updater.start_polling()

#updater.stop_polling()
