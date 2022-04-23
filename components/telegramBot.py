# -*- coding: utf-8 -*-
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5144076007:AAHJhADh1U-XjFw4ilsxDcvhknnrc6UyJj0'
    bot_chatID = '1271349182'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()