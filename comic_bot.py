import comic_scrapers as cs
import comic_utils as cu
import pickle

from telegram.ext import Updater, CallbackQueryHandler, ConversationHandler
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import ChatAction, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup


api_dict = None
with open('/home/uday/telegram_api.key', 'rb') as f:
    api_dict = pickle.load(f)
Api_Key = api_dict['key']

updater = Updater(token=Api_Key)
dispatcher = updater.dispatcher

custom_keyboard = [['Another Random Strip'], ['Random From A Specific Comic']]
reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)

# TODO INcase of TIMEOUT Send some message


def start(bot, update):
    random_grab = cu.random_grab()
    try:
        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)
        bot.send_photo(chat_id=update.message.chat_id,
                       photo=random_grab.get_random(), reply_markup=reply_markup)
        bot.send_message(chat_id=update.message.chat_id, text=str(
            random_grab.details), disable_web_page_preview=True)
    except Exception as e:
        print('something went wrong at start\n',
              e, '\n', +str(random_grab.name))
        bot.send_message(chat_id=update.message.chat_id,
                         text="something went wrong [0]" + str(random_grab.name))


def clear_keyboard(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id,
                         action=ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="keyboard removed", reply_markup=ReplyKeyboardRemove())


def message(bot, update):
    random_grab = cu.random_grab()
    sent = False
    try:
        bot.send_chat_action(chat_id=update.message.chat_id,
                             action=ChatAction.TYPING)
        pic = random_grab.get_random()
        if update.message.text == custom_keyboard[0][0]:
            bot.send_photo(chat_id=update.message.chat_id,
                           photo=pic, reply_markup=reply_markup)
            sent = True
        elif update.message.text == custom_keyboard[1][0]:
            button_list = [InlineKeyboardButton(
                cu.comic_details[a].name, callback_data="hi") for a in cu.grabers]
            in_reply_markup = InlineKeyboardMarkup(
                cu.build_menu(button_list, n_cols=2))
            bot.send_message(chat_id=update.message.chat_id,
                             text="Select a comic", reply_markup=in_reply_markup)
        else:
            bot.send_message(chat_id=update.message.chat_id,
                             text="I no understand what you say, but here's a comic strip :)")
            bot.send_photo(chat_id=update.message.chat_id,
                           photo=pic, reply_markup=reply_markup)
            sent = True
        if sent:
            bot.send_message(chat_id=update.message.chat_id, text=str(
                random_grab.details), disable_web_page_preview=True)
    except Exception as e:
        print('something went wrong at message at \n', e)
        bot.send_message(chat_id=update.message.chat_id,
                         text="something went wrong [1]" + str(random_grab.name))

def callback_message(bot, update):
    random_grab=cu.comic_graber_names[update.callback_query.data]
    try:
        bot.send_chat_action(chat_id=update.message.chat_id,
                                action=ChatAction.TYPING)
        bot.send_photo(chat_id=update.message.chat_id,
                        photo=random_grab.get_random(), reply_markup=reply_markup)
        bot.send_message(chat_id=update.message.chat_id, text=str(
            random_grab.details), disable_web_page_preview=True)
    except Exception as e:
        print('something went wrong at start\n',
                e, '\n', +str(random_grab.name))
        bot.send_message(chat_id=update.message.chat_id,
                        text="something went wrong [0]" + str(random_grab.name))

start_handler = CommandHandler('start', start)
ck_handler = CommandHandler('ck', clear_keyboard)
message_handler = MessageHandler(Filters.text, message)
callback_message_handler = CallbackQueryHandler(callback_message)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(ck_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(callback_message_handler)
updater.start_polling()
print("started")

# updater.start_webhook(listen='0.0.0.0',
#                       port=8443,
#                       url_path='TOKEN',
#                       key=Api_Key,
#                       cert='~/cert.pem',
#                       webhook_url='https://www.roughbots.xyz:8443/TOKEN')
# updater.stop_polling()
