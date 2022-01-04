import re
import requests
import json

from os import stat
from time import sleep
from bs4 import BeautifulSoup

import artic

NEWS_URL = 'https://www.ufms.br/category/noticias/page/'

post_id_list = []
pages = []


# Get news pages
for i in range(1,3):
    tmp = NEWS_URL + str(i) + '/'
    pages.append(tmp)

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
            if not artic.exist_article(data, post_id):
                exist_new_article = True
                artic.post_article(post_id, title, datetime, content_preview, link)


if exist_new_article:
    with open('last_posts_id.json', 'w') as outfile:
        json.dump(post_id_list, outfile)
