import re
import requests
from time import sleep

BOT_TOKEN = 'INSERT_BOT_TOKEN_HERE'
CHANNEL_ID = 'INSERT CHANNEL ID OR USERNAME'

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

    message ="*{titulo}*\n\n{datetime}\n\n_{content}_\n\n[LEIA MAIS]({url})\n\n\#post\_{ID}".format(
        titulo = title, 
        datetime = time, 
        content = content, 
        url = url, 
        ID= id_
    )
    r = requests.get(api_url + 'sendMessage', data={"chat_id":CHAT_TARGET,"text":message, "parse_mode":"MarkdownV2"})
    response = r.json()

    if(response['ok'] is True):
        print("[SUCCESSFUL] REQUEST POST ID: {}\n".format(ID))
    else:
        print("[FAILED] REQUEST POST ID: {}\n".format(ID))

    sleep(delay)


