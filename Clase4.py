#Crear un entorno virtual con virtualenv -p python ,crear el nombre del entorno virtual Ex:Clase4
#instalar con sudo apt install
#ir a la raiz y poner Spurce ativate 
#Machine learning: aprendizaje supervisado #Deep learning : aprenidzaje no supervisado
# top down : es basado en sensores o caracteristicas para jutificar la falta de conocimiento
# botton down: *es una inteligencia supervisada a la cual se le puede entrenar o ensenar.
#             *puede ser no supervisado: es la inteligencia que se retro alimenta a base de estadisticas 
#jupyter-notebook - password greencore
#Anaconda es un suit para la ciencia de datos y analisis-> Jupyter es una herramienta para explicar codigo
#Red neuronal  XOR -> de dos capas.
#con un INPUT , capas y output.
#funciones logisticas de Sigmone

#****************************************************#

#import numpy as np
#from keras.models import Sequential
#from keras.layers.core import Dense

##cargamos las 4 conbinaciones de las compuertas XOR
#training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")

##y estos son los resultados que se obtienen, en el mismo orden
#target_data = np.array([[0],[1],[1],[0]], "float32")

#model = Sequential()
#model.add(Dense(16, input_dim=2, activation='relu'))
#model.add(Dense(1, activation='sigmoid'))

#model.compile(loss='mean_squared_error',
 #            optimizer='adam',
  #           metrics=['binary_accuracy'])

#model.fit(training_data, target_data, epochs=1000)

# evaluamos el modelo
#scores = model.evaluate(training_data, target_data)
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#print(model.predict(training_data).round())