import re
from time import sleep
from app.credentials import BOT_TOKEN, CHAT_TARGET

from bot import Bot

bot = Bot(BOT_TOKEN)

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

    bot.send_message(CHAT_TARGET, message)

    sleep(delay)


