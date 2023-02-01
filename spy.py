from datetime import datetime
from aiogram import types

def spy(message):
    user = []
    user.append(datetime.now())
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user.append(message.text)
    user = list(map(str, user))
    with open('spy.txt', 'a', encoding='UTF-8') as data:
        data.write(' | '.join(user) + '\n')