# -*- coding: utf-8 -*-
"""
Track stream
@author: neylson.crepalde
"""
from twython import TwythonStreamer, Twython, TwythonError
import time
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

saida = open('collected_tweets.txt',mode='w')

post = Twython(
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
            message = "@{}: {}".format(username, tweet)
            if username == 'botedsuperior':
                #Não printa nem retweeta posts do próprio bot
                print('segue...')
            else:
                print(message)
                saida.write(str(data) + '\n')
                            
                if 'RT @' not in message:
                    #Se não for RETWEET
                    try:
                        post.update_status(status = message[:140])
                        print('Foi tweetado!')
                    except TwythonError as e:
                        print(e)
                    time.sleep(10)

                    
            
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

#ids = [344956335,44502932,42399225,22037917] melhor para pós-graduação

ids = [2850190966,56780945,14595207,62703362]

keys = ['ensino superior','educação superior','ensino universitário','#educaçãosuperior',
        '#educacaosuperior','#ensinosuperior']
stream.statuses.filter(track=keys, follow=ids)
