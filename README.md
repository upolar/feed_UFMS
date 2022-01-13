# FEED UFMS

## About this project

A initial project to practice webscraping with python on the college website. 
The project extract the news and post it on a Telegram Channel. 


### First steps

### Configuration and usage

First of all install the `requirements.txt` with pip or others. 
I recommend to use a virtual env to avoid package version conflict. 

Activate your virtual env (if u have one) and type:

`pip install -r requirements.txt`

Now you should be able to execute the script and scrap the UFMS News page.
But to the bot be able to realize a post you should edit two variables 
`BOT_TOKEN` and `CHAT_TARGET`. 
Even without these credentials the script will be able to 
get the news from the website.

| variable | Description |
| ---  | --- |
| `BOT_TOKEN` | To get a bot token, create a bot in [@botfather](https://t.me/botfather)|
| `CHAT_TARGET` | The chat identifier ("@username" or ID) where the bot will post the news if it has enough permissions |


Execute the `app/main.py` inside your virtual env and just wait. :) 
