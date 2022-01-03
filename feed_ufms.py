import requests
import json
import re

from time import sleep
from bs4 import BeautifulSoup
from os import stat

BOT_TOKEN = "INSERT_BOT_TOKEN_HERE"
CHAT_TARGET = "INSERT CHANNEL ID OR USERNAME"

api_url = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'
news_url = 'https://www.ufms.br/category/noticias/page/'

new_data = {}
new_data['News'] = []

pages = []


# Get news pages
for i in range(1,3):
    tmp = news_url + str(i) + '/'
    pages.append(tmp)

def exist_article(data, value):
    if(data is None):
        return False
    return any(new['ID']==value for new in data['News'])

def create_article_list(ID, title, time, content, url):
    return new_data['News'].append({
                'ID': ID,
                'title': title,
                'content': content,
                'timestamp': time,
                'website': url
                })

def post_article(ID, title, time, content, url, delay=10):
    pattern = r'([\_|\*|\[|\]|\(|\)|\~|\`|\>|\#|\+|\-|\=|\||\{|\}|\.|\!])'
    title = re.sub(pattern, r'\\\1', title)
    content = re.sub(pattern, r'\\\1', content)
    time = re.sub(r'\-', r'\\-', time)

    message ="*{titulo}*\n\n{datetime}\n\n_{content}_\n\n[LEIA MAIS]({url})\n\n\#post\_{ID}".format(
        titulo = title, 
        datetime = time, 
        content = content, 
        url = url, 
        ID= ID
    )
    r = requests.get(api_url + 'sendMessage', data={"chat_id":CHAT_TARGET,"text":message, "parse_mode":"MarkdownV2"})
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
        ID = int(re.sub(r'post\-', r' ', article.get('id')))
        title = article.find('h2').getText()
        datetime = article.find('time').get('datetime')
        content_preview = article.find('p').getText()
        link = article.find('a').get('href')
     
        with open("news.json") as f:
            data = json.load(f)
            
            create_article_list(ID, title, datetime, content_preview, link)
            
            # Post article / send message only if NOT exist
            if not exist_article(data, ID):
                exist_new_article = True
                post_article(ID, title, datetime, content_preview, link)


if(exist_new_article):
    with open('news.json', 'w') as outfile:
        json.dump(new_data, outfile)
