import re
import requests
from time import sleep
from credentials import BOT_TOKEN, CHAT_TARGET

API_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

def exist_article(data, value):
    return any(new==value for new in data)

def create_article_list(id_):
    return new_data.append(id_)

def post_article(id_, title, time, content, url, delay=10):
    pattern = r'([\_|\*|\[|\]|\(|\)|\~|\`|\>|\#|\+|\-|\=|\||\{|\}|\.|\!])'
    title = re.sub(pattern, r'\\\1', title)
    content = re.sub(pattern, r'\\\1', content)
    time = re.sub(r'\-', r'\\-', time)

    message = f"*{title}*\n\n{time}\n\n_{content}_\n\n[LEIA MAIS]({url})\n\n\#post\_{id_}"

    r = requests.get(API_URL + 'sendMessage', data={"chat_id":CHAT_TARGET,"text":message, "parse_mode":"MarkdownV2"})
    response = r.json()

    if(response['ok'] is True):
        print(f"[SUCCESSFUL] REQUEST POST ID: {id_}\n")
    else:
        print(f"[FAILED] REQUEST POST ID: {id_}\n")

    sleep(delay)


