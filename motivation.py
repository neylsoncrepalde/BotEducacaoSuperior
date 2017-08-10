"""
Posts de motivação
Bot Educação Superior
@author: neylson.crepalde
"""
from twython import Twython
import random
import time
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

messages = ["Aprender é a única coisa que a mente nunca se cansa, nunca tem medo e nunca se arrepende!",
            "Aquele que não luta pelo futuro que quer, deve aceitar o futuro que vier!",
            "Ter sucesso é falhar repetidamente, mas sem perder o entusiasmo!",
            "Não importa o quão devagar você vá, desde que você não pare!",
            "Descobri que quanto mais eu estudo, mais sorte eu pareço ter nas provas!",
            "É fazendo que se aprende, aquilo que se deve aprender a fazer!",
            "Nenhum obstáculo é tão grande se sua vontade de vencer for maior!",
            "Há cinco degraus para se alcançar a sabedoria: Calar, ouvir, lembrar, sair, estudar.",
            "Comece onde está. Use o que você tem. Faça o que puder!",
            "O sucesso normalmente vem para quem está ocupado demais para pensar nele!",
            "Você já observou um homem habilidoso em seu trabalho? Será promovido ao serviço real; não trabalhará para gente obscura."]

pics = ['chapeu.jpeg','chapeu2.jpg','chapeu3.jpg','chapeu4.jpg','ensinosuperior.jpg',
        'estudante.jpg','estudante2.jpg','estudante3.jpg','estudante4.jpg','livro.jpg','net.jpg']

while True:
    with open(random.choice(pics), 'rb') as photo:
        twitter.update_status_with_media(status=random.choice(messages), media=photo)
    print("Tweet postado!")
    time.sleep(17280)

