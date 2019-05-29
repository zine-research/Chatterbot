from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('scala')
trainer = ListTrainer(bot)

for files in os.listdir('C:\\Users\\tanishk\\Downloads\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english'):
    data = open('C:\\Users\\tanishk\\Downloads\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english\\' + files, 'r').readlines()
    trainer.train(data)

while True:
    user_input = input('you:')
    try:
        if user_input.split() != 'bye' or user_input.split() != 'Bye':
            reply = bot.get_response(user_input)
            print('scala', reply)
        if user_input.split() == 'bye' or user_input.split() == 'Bye':
            print('scala: BYE')
            break
    except:
        print("Can you type in another format!! please...")
