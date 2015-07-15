import requests
import json

from bot_url import URL
from model import Update


def get_updates(offset):
    response = json.loads(requests.get(URL + "getUpdates?offset={0}".format(offset)).text)
    assert response["ok"]
    return map(Update, response["result"])


def send_message(chat_id, text):
    return json.loads(requests.get(URL + u"sendMessage?chat_id={0}&text={1}".format(chat_id, text)).text)
