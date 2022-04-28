import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def lineNotifyMessage(msg):
    token = os.environ.get("LINE_NOTIFY_TOKEN")
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code