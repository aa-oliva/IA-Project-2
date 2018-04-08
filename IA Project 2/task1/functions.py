# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:34:01 2018

@author: aa-ol
"""

import random, re

#Funcion para que todas las letras sean minusculas11
def sanitizar(cadena_entrada):
    return ((re.sub('[^A-Za-z0-9 \t]+', '', cadena_entrada)).lower())

#Funcion para abrir archivos txt y guardarlos linea por linea
def getText(file_name):
    matriz = []
    data = [sanitizar(line.strip()) for line in open(file_name, 'r', encoding="utf8")]
    
    for i in range (len(data)):
        line = []
        x,y = data[i].split("\t")
        line.append(x)
        line.append(y)
        matriz.append(line)
    return matriz

def trainingSample(matriz, percentage):
    training = []
    for _ in range (0, int((len (matriz))*percentage)):
        training.append(matriz.pop(random.randrange(0, len(matriz))))
        return training
