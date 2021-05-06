#Adi Faintuch, 5/4/21
import os
from twilio.rest import Client

import requests
# from py_imessage import imessage
from time import sleep
import urllib.parse
import json
import os


phone_to = input("Enter authorized phone number in the format +1XXXXXXXXXX: ") #make sure it is in the format '+1XXXXXXXXXX'
phone_from = '' #enter your twilio phone number in the format '+1XXXXXXXXXX'

account_sid = '' #enter your twilio account_sid
auth_token = '' #enter your twilio auth_token
client = Client(account_sid, auth_token)

err_message = "Too Many Requests: Rate limit of 5 requests per hour exceeded"

text_to_translate = input("Enter text message: ")
url_encoded = urllib.parse.quote(text_to_translate)
url = "http://api.funtranslations.com/translate/yoda?text=" + url_encoded

x = requests.get(url);
dict = x.json()

if("error" in dict):
    print(dict["error"]["message"])
else:
    translated = dict["contents"]["translated"]
    message = client.messages.create(
                                  body=translated,
                                  from_=phone_from,
                                  media_url=['https://themodernjedi.files.wordpress.com/2012/01/yoda.png'],
                                  to=phone_to
                              )



# print(message.sid)
