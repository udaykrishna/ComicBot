import comic_scrapers as cs
import pickle

from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler,Filters
from telegram import ChatAction,ReplyKeyboardMarkup

api_dict=None
with open('/home/uday/telegram_api.key','rb') as f:
    api_dict=pickle.load(f)
Api_Key=api_dict['key']

updater=Updater(token=Api_Key)
dispatcher=updater.dispatcher

custom_keyboard=[['Another Random Strip']]
reply_markup=ReplyKeyboardMarkup(custom_keyboard,resize_keyboard=True)

def start(bot, update):
    random_grab=cs.random_grab()
    try:
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        bot.send_photo(chat_id=update.message.chat_id,photo=random_grab.get_random(),reply_markup=reply_markup)
        bot.send_message(chat_id=update.message.chat_id,text=str(random_grab.details),disable_web_page_preview=True)
    except Exception as e:
        print('something went wrong at start\n',e)
        bot.send_message(chat_id=update.message.chat_id,text="something went wrong")

def message(bot,update):
    random_grab=cs.random_grab()
    try:
        bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        pic=random_grab.get_random()
        if update.message.text == custom_keyboard[0][0]:
            bot.send_photo(chat_id=update.message.chat_id,photo=pic,reply_markup=reply_markup)
        else:
            bot.send_message(chat_id=update.message.chat_id,text="I no understand what you say, but here's a comic strip :)")
            bot.send_photo(chat_id=update.message.chat_id,photo=pic,reply_markup=reply_markup)
        bot.send_message(chat_id=update.message.chat_id,text=str(random_grab.details),disable_web_page_preview=True)
    except Exception as e:
        print('something went wrong at message\n',e)
        bot.send_message(chat_id=update.message.chat_id,text="something went wrong")

start_handler=CommandHandler('start',start)
message_handler=MessageHandler(Filters.text,message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)
updater.start_polling()

#updater.stop_polling()
