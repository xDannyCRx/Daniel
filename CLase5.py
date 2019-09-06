#esta funcion 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def crearbot(): #crea una funcion con el nombre de creabot
    proyecto = input('Nombre del chatbot: ') # asigne un mobre al proyecto
    os.mkdir(proyecto)
    #crea un carpeta con nombre de proyecto una sub carpeta de nombre proyecto
    os.mkdir(proyecto+'/'+proyecto)
    namechatbot = './'+proyecto+'/'+proyecto+'.yml'
    #concarteracion: une stream con variables
    file = open(namechatbot, 'w') \
    #abre el archivo ya creado con .YML

    categoria = input('Escriba una categoria: ')
    #el agregar categorias ayuda a la precision a la hora de buscar informacion
    file.write('categoria:' + os.linesep)
    file.write('-' + categoria + os.linesep)
# - es la resuesta a un estimulo -- esto es un estimulo 
    while True:
        continuar = input('Desea agegar otra: \n 1-Agregar \n 2-Terminar ')
        if continuar == '1':
            pregunta = input('Pregunta ')
            respuesta = input('Respuesta ')

            file.write('-- '+ pregunta + os.linesep)
            file.write('- '+ respuesta + os. linesep)

        if continuar == '2':
            file.close()
            break
    namechatbot = './'+proyecto+'/'+proyecto+'.py'
    file = open(namechatbot, 'w')
    file.write("from chatterbot import ChatBot\nfrom chatterbot.trainer import ListTrainers\nimport os\nbot=ChatBot('"+proyecto+"')\ntrainer = ListTrainer(bot)\n" + os.linesep)
    file.write("for files in os.listdir('./"+proyecto+"/'): \n data=open('./"+proyecto+"/'+files, 'r').readlines()\n trainer.train(data)\n trainer.train(data)\n trainer.train(data)\n"+os.linesep)
    file.close()
 
crearbot()

#import.os
#os.system('python --version")