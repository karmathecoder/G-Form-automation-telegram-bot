from telegram import Update
from telegram.ext import CallbackContext

from telegram_msg import *
from db import *
from payload_model import *
from form import *

import os
from dotenv.main import load_dotenv
load_dotenv()

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello , See How to Use https://graph.org/How-To-Use-Auto-Placement-Attendance-Bot-03-04")
    send_msg(os.environ['admin'],"Bot started by :" + str(update.message.chat_id)+ "\n"+ str( update.message.chat['username']+ "\n" + update.message.chat['first_name']+ " "+update.message.chat['last_name']))

def add(update: Update, context: CallbackContext):
    msg = update.message.text
    user_id = update.message.chat_id
    msg = msg.split(" ",1)
    if len(msg)== 2:
        try :
            data_tuple = (user_id,)+ eval(msg[1])
            x = insertion_table('info',data_tuple)
            context.bot.send_message(chat_id=update.effective_chat.id, text=x)
            context.bot.send_message(chat_id=update.effective_chat.id, text=view_chatid_data(user_id))
            context.bot.send_message(chat_id=update.effective_chat.id, text="Keep Bot on UNMUTE to recive nortification")
        except:
            context.bot.send_message(chat_id=update.effective_chat.id, text="data insertion failure")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Use Proper Format get from /help")
        try:
            online_mysql_insertion(data_tuple)
            send_msg(os.environ['admin'],f"data insertion-> {data_tuple}")
        except:
            send_msg(os.environ['admin'],"data insertion failure")

    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Use Proper Format get from /help")
        context.bot.send_message(chat_id=update.effective_chat.id, text="/add ('abc@gmail.com',12020009022xxx,'Tony Stark',304202000900xxx,6256868xxx)")

def delete(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    try:
        x = table_data_deletion(user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=x)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error Contact Admin @featkarma_pm_bot")

def update_detail(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="This Feature Comming Soon")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Till then , First Delete Info using /delete then Add using /add")
    context.bot.send_message(chat_id=update.effective_chat.id, text="For more Info Use /help")

def show_detail(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    try :
        context.bot.send_message(chat_id=update.effective_chat.id, text=view_chatid_data(user_id))
    except:        
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error! Pls Add data first using /add")

def admin_local_query(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    env_admin = int(os.environ['admin'])
    msg = update.message.text
    msg = msg.split(" ",1)
    if user_id == env_admin:
        if len(msg)==2:
            query_sent = msg[1]
            try:
                data_ret = local_mysql_query(query_sent)
                context.bot.send_message(chat_id=update.effective_chat.id, text=data_ret)
            except:        
                context.bot.send_message(chat_id=update.effective_chat.id, text="Error execution")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No Query passed")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You dont have admin rights")

def admin_execution_query(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    msg = update.message.text
    env_admin = int(os.environ['admin'])
    msg = msg.split(" ",1)
    if user_id == env_admin:
        if len(msg)==2:
            query_sent = msg[1]
            try:
                data_ret = online_mysql_query(query_sent)
                context.bot.send_message(chat_id=update.effective_chat.id, text=data_ret)
            except:        
                context.bot.send_message(chat_id=update.effective_chat.id, text="Error execution")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No Query passed")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You dont have admin rights")

def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="https://graph.org/How-To-Use-Auto-Placement-Attendance-Bot-03-04")

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


#form functions
def formstatus(update: Update, context: CallbackContext):
    url = os.environ['formurl']
    context.bot.send_message(chat_id=update.effective_chat.id, text=form_on_off(url))

def prefilledlink(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    try:
        prefilledurl_base = os.environ['prefilledurl']
        context.bot.send_message(chat_id=update.effective_chat.id, text=prefilled_link_gen(user_id,prefilledurl_base))
    except:        
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error! Pls Add data first using /add")

def submit(update: Update, context: CallbackContext):
    url = os.environ['formurl']
    status = form_on_off(url)
    user_id = update.message.chat_id
    try:
        if status == "Form Close":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Form Is Closed, Cant Submit")
        
        elif status == "Form OPEN":
            try :
                data = gen_payload_model_user(user_id)
                sub_status = submit_form(url,data)
                context.bot.send_message(chat_id=update.effective_chat.id, text=sub_status)
            except :
                context.bot.send_message(chat_id=update.effective_chat.id, text="Error On Submission")
        
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Function Error")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sending Prefilled Url")
            prefilledurl_base = os.environ['prefilledurl']
            context.bot.send_message(chat_id=update.effective_chat.id, text=prefilled_link_gen(user_id,prefilledurl_base))

    except:        
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error! Pls Add data first using /add")
