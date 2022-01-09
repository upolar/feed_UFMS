import re
import requests
import json

from time import sleep
from bs4 import BeautifulSoup

from modules.articles import exist_article, format_post_content, create_post

NEWS_URL = 'https://www.ufms.br/category/noticias/page/'

post_id_list = []

# Get news pages
def get_pages():
    pages = []
    for i in range(1,3):
        tmp = NEWS_URL + str(i) + '/'
        pages.append(tmp)

    return pages

exist_new_article = False

def get_article_list():
    pages = get_pages()
    for item in reversed(pages):
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')
        art_list = soup.findAll('article')

    return art_list
    
def main(): 
    global exist_new_article
    articles_list = get_article_list()

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
                msg = format_post_content(post_id, 
                        title, 
                        datetime, 
                        content_preview, 
                        link)

                create_post(msg)

def update_post_list_file():
    with open('last_posts_id.json', 'w') as outfile:
        json.dump(post_id_list, outfile)   

if __name__ == '__main__':
    main()

    print(exist_new_article)
    
    if exist_new_article:
        update_post_list_file()
