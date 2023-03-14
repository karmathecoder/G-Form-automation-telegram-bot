from db import *
from urllib.parse import urlencode
import os
from dotenv.main import load_dotenv
load_dotenv()

gform_entry = eval(os.environ['mainentryid'])

def gen_payload_model():
    sqdata = view_data('info')
    res = []
    for i in sqdata:
        payload_model = {
            gform_entry[0] : i[1],
            gform_entry[1] : i[2],
            gform_entry[2] : i[3],
            gform_entry[3] : i[4],
            gform_entry[4] : "CST",
            gform_entry[5] : "2020 - 2024",
            gform_entry[6] : i[5],
        }
        res.append([i[0],payload_model])
    return res

def gen_payload_model_user(chat_id):
    data = view_chatid_data(chat_id)
    payload_model = {
                'usp': 'pp_url',
                gform_entry[0] : data[0],
                gform_entry[1] : data[1],
                gform_entry[2] : data[2],
                gform_entry[3] : data[3],
                gform_entry[4] : "CST",
                gform_entry[5] : "2020 - 2024",
                gform_entry[6] : data[4],
            }
    return payload_model


def prefilled_link_gen(chat_id,base_url):
    data = view_chatid_data(chat_id)
    payload = {
                'usp': 'pp_url',
                gform_entry[0] : data[0],
                gform_entry[1] : data[1],
                gform_entry[2] : data[2],
                gform_entry[3] : data[3],
                gform_entry[4] : "CST",
                gform_entry[5] : "2020 - 2024",
                gform_entry[6] : data[4],
            }
    encoded_payload = urlencode(payload)
    url = f'{base_url}?{encoded_payload}'
    
    return url