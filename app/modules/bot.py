import requests
import logging

class Bot():
    bot = requests.Session()

    def __init__(self, token):
        self.API_LINK = f"https://api.telegram.org/bot{token}/"

    """ 
        CHAT - Chat ID
        msg - message to be send
        Reply_id - message to be replied
        allow_sending_without_reply - True if the message should be sent even if the specified replied-to message is not found
        Protect_content - protect the content of the sent message from forwarding and saving
        parse_mode
    """ 
    def send_message(self, chat, msg, reply_id="", allow_sending_without_reply=True, reply_markup={}, protect_content=False, parse_mode="MarkdownV2"):
        r =  self.bot.get(self.API_LINK + 'sendMessage', 
               json={"chat_id": chat,
                     "text": msg,
                     "reply_to_message_id": reply_id,
                     "allow_sending_without_reply": allow_sending_without_reply,
                     "reply_markup": reply_markup,
                     "protect_content": protect_content,
                     "parse_mode": parse_mode}
               ).json()
        
        if not r['ok']:
            logger = logging.getLogger(__name__)

            syslog = logging.StreamHandler()
            filelog = logging.FileHandler('app.log', 'a')
            
            formatter = logging.Formatter('%(asctime)s - [%(levelname)s] : %(message)s')
            #syslog.setFormatter(formatter)
            
            filelog.setFormatter(formatter)
            logger.addHandler(filelog)

            error_message = f"{r['error_code']} - {r['description']}"
            
            logger.error(error_message)
            
        return r['ok']
