# -*- coding: utf-8 -*-
"""
Olá mundo! Teste
Bot Educação Superior
@author: neylson.crepalde
"""
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
message = "Olá Mundo!"
#twitter.update_status(status=message)
#print("Tweeted: {}".format(message))

'https://pbs.twimg.com/profile_images/717482045019136001/aYzlNG5L.jpg'

message = "Muito trabalho pela frente!"
with open('C:/Users/neylson.crepalde/Pictures/aYzlNG5L.jpg', 
          'rb') as photo:
    twitter.upload_media(status=message, media=photo)
print("Tweet ok!")