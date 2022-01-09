import re
from time import sleep

from bot import Bot
from credentials import BOT_TOKEN, CHAT_TARGET

from modules.bot import Bot

bot = Bot(BOT_TOKEN)

def exist_article(data, value):
    return any(new==value for new in data)

def format_post_content(id_, title, time, content, url):
    pattern = r'([\_|\*|\[|\]|\(|\)|\~|\`|\>|\#|\+|\-|\=|\||\{|\}|\.|\!])'
    title = re.sub(pattern, r'\\\1', title)
    content = re.sub(pattern, r'\\\1', content)
    time = re.sub(r'\-', r'\\-', time)

    message = f"*{title}*\n\n{time}\n\n_{content}_\n\n[LEIA MAIS]({url})\n\n\#post\_{id_}"

    bot.send_message(CHAT_TARGET, message)
    return message

def create_post(msg, delay=10):
    bot.send_message(CHAT_TARGET, msg)

    sleep(delay)


