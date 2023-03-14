import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_func import *

#Enable Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(token=os.environ['API_key'],use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))

dp.add_handler(CommandHandler('add',add))
 
dp.add_handler(CommandHandler('delete',delete))

dp.add_handler(CommandHandler('update',update_detail))

dp.add_handler(CommandHandler('view',show_detail))

dp.add_handler(CommandHandler('adminlocal', admin_local_query))

dp.add_handler(CommandHandler('adminquery', admin_execution_query))

dp.add_handler(CommandHandler('help',help))

#form commands
dp.add_handler(CommandHandler('status',formstatus))

dp.add_handler(CommandHandler('prefill',prefilledlink))

dp.add_handler(CommandHandler('submit',submit))


dp.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()
