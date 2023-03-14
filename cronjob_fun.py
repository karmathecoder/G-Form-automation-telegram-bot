from form import *
from telegram_msg import *
from payload_model import *

import schedule
import time

import os
from dotenv.main import load_dotenv
load_dotenv()

def auto_submit():
    payload = gen_payload_model()
    url = os.environ['formurl']
    base_url = os.environ['prefilledurl']
    
    if form_on_off(url)=="Form OPEN":
        for i in payload:
            send_msg_norti(i[0],"Form OPEN")
            try:
                data = submit_form(url,i[1])
                send_msg_norti(i[0],data)
                send_msg_norti(i[0],prefilled_link_gen(i[0],base_url))
            except:
                send_msg_norti(i[0],prefilled_link_gen(i[0],base_url))
        time.sleep(500)
    return 0

# auto_submit(gen_payload_model())

schedule.every(6).seconds.do(auto_submit)
while True:
 
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
            