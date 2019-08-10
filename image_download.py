import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig()
###

def dl_image(bot, update):
    file = bot.getFile(update.message.photo[-1].file_id)
    print(file.file_path[86:])
    file.download(file.file_path[86:])

updater = Updater("931314772:AAGe72UZCsLLLXKBj08StzQKdUopXv5Z6uY")
updater.dispatcher.add_handler(MessageHandler(Filters.photo, dl_image))
updater.start_polling()
updater.idle()