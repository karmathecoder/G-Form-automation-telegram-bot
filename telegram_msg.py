import requests
from dotenv.main import load_dotenv
import os
load_dotenv()
api_key = os.environ['API_key_norti']
api_key_main = os.environ['API_key']

def send_msg(chat_id,msg):
    endpoint = f"https://api.telegram.org/bot{api_key}/sendMessage"
    parameters = {'chat_id':chat_id,'text':msg}
    requests.get(url = endpoint, params = parameters)

def send_msg_norti(chat_id,msg):
    endpoint = f"https://api.telegram.org/bot{api_key_main}/sendMessage"
    parameters = {'chat_id':chat_id,'text':msg}
    requests.get(url = endpoint, params = parameters)
