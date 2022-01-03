import re
import requests
import json

from os import stat
from time import sleep
from bs4 import BeautifulSoup

BOT_TOKEN = 'INSERT_BOT_TOKEN_HERE'
CHANNEL_ID = 'INSERT CHANNEL ID OR USERNAME'
API_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'
NEWS_URL = 'https://www.ufms.br/category/noticias/page/'

post_id_list = []
pages = []


# Get news pages
for i in range(1,3):
    tmp = NEWS_URL + str(i) + '/'
    pages.append(tmp)

def exist_article(data, value):
    if(data is None):
        return False
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
    r = requests.get(API_URL + 'sendMessage', data={"chat_id":CHAT_TARGET,"text":message, "parse_mode":"MarkdownV2"})
    response = r.json()

    if(response['ok'] is True):
        print("[SUCCESSFUL] REQUEST POST ID: {}\n".format(ID))
    else:
        print("[FAILED] REQUEST POST ID: {}\n".format(ID))

    sleep(delay)

exist_new_article = False

for item in reversed(pages):
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')
    articles_list = soup.findAll('article')
    
    
    # Append article from the oldest to newest
    for article in reversed(articles_list):
        post_id = int(re.sub(r'post\-', r' ', article.get('id')))
        title = article.find('h2').getText()
        datetime = article.find('time').get('datetime')
        content_preview = article.find('p').getText()
        link = article.find('a').get('href')
     
        with open("last_posts_id.json") as f:
            data = json.load(f)
            
            post_id_list.append(post_id)

            # Post article / send message only if NOT exis
            if not exist_article(data, post_id):
                exist_new_article = True
                #post_article(post_id, title, datetime, content_preview, link)


if exist_new_article:
    with open('last_posts_id.json', 'w') as outfile:
        json.dump(post_id_list, outfile)
