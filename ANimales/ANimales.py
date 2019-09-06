from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('ANimales')
trainer = ListTrainer(bot)

for files in os.listdir('./ANimales/'):
    data=open('./ANimales/'+files, 'r').readlines()
    trainer.train(data)
    trainer.train(data)
    trainer.train(data)

while True:
    message=input('\t\t\tYou')
    if message.strip()!='Bye' or 'bye':
        replay=bot.get_response(message)
        print('disfrutomisalud:', replay)
    if message.strip()=='Bye':
        print('Disfrutomisalud: Bye')
        break