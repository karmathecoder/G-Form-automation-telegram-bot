import requests
from bs4 import BeautifulSoup
from lxml import etree

def submit_form(url,Data):
    try:
        res = requests.post(url, data = Data)
        if res.status_code == 200:
            return "Sucessfully Submitted"
        else:
            return f"Error Occured StatusCode {res.status_code}"
    except:
        return "Error Occured"

def form_dom(url):
    htm = requests.get(url)
    soup= BeautifulSoup(htm.content, "html.parser")
    dom = etree.HTML(str(soup))
    return dom

def form_on_off(url):
    dom = form_dom(url)
    try:
        close = dom.xpath('//div[@class="UatU5d"]')[0].text
        res = close.find('no longer accepting responses')
        if res != -1:
            return "Form Close"
    except:
        return "Form OPEN"
