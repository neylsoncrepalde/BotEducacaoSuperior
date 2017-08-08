# -*- coding: utf-8 -*-
"""
Track stream
@author: neylson.crepalde
"""
from twython import TwythonStreamer
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            #Modificar instruções para armazenamento, filtragem e retweet
            print("@{}: {}".format(username, tweet))
            

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

stream.statuses.filter(track='ensino superior')


