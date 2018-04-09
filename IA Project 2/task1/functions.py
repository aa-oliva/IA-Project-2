# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:34:01 2018

@author: aa-ol
"""

import random, re

# Function so that all the letters are lowercase
def sanitizar(string_input):
    return ((re.sub('[^A-Za-z0-9 \t]+', '', string_input)).lower())

# Function to open txt files and save them line by line
def getText(file_name):
    matrix = []
    data = [sanitizar(line.strip()) for line in open(file_name, 'r', encoding="utf8")]
    
    for i in range (len(data)):
        line = []
        x,y = data[i].split("\t")
        line.append(x)
        line.append(y)
        
        matrix.append(line)
    return matrix

# Function to separate the data by percentage and  obtain a sample
def trainingSample(matrix, percentage):
    training_sample = []
    for _ in range (0, int((len (matrix))*percentage)):
        training_sample.append(matrix.pop(random.randrange(0, len(matrix))))
    return training_sample

# Function to classify what type of data is per line according to flag
def classifyMessages(matrix, label):
    spam = []
    ham = []
    for i in range(len(matrix)):
        label = matrix[i]
        if(label[0]=="spam"):
            spam.append(label[1])
        if (label[0]=="ham"):
            ham.append(label[1])
    
    return spam, ham

# Function to obtain the unique words of each list
def getUniqueWords(array):
    unique = []
    for i in range(len(array)):
        phrase = array[i].split(" ")
        for word in phrase:
            if word not in unique:
                unique.append(word)
    return unique

# Function to obtain only the list of a column
def getColumn(matrix, column_num):
    column = []
    for i in range(len(matrix)):
        label = matrix[i]
        column.append(label[column_num])
    return column 

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
    """
INPUT: int K, string palabra, array tipo_palabra, int palabras_totales
"""
def laplaceSmoothingBasic(k, palabra, tipo_palabra, palabras_totales):
    cant_ocurrencia = 0.0
    cant_observaciones = len(tipo_palabra)
    for i in range(len(tipo_palabra)):
        if tipo_palabra[i]==palabra: cant_ocurrencia +=1
    return ((cant_ocurrencia + k)/(cant_observaciones + k*palabras_totales))

"""
INPUT: array string mensajes, int k, array tipo_palabra, int palabras_totales
"""
def probabilidadOracion(mensaje, k, tipo_palabra, palabras_totales):
    probabilidad = 1.0
    for i in range(len(mensaje)):
        probabilidad =  probabilidad * laplaceSmoothingBasic(k, mensaje[i], tipo_palabra, palabras_totales)
    return probabilidad

"""
INPUT: matriz grupo, string tipo, int k
"""
def probabilidadMain(grupo, tipo, k):
    cant_ocurrencia = 0.0
    cant_observaciones = len(grupo)
    for i in range(len(grupo)):
        tupla = grupo[i]
        if(tupla[0]==tipo): cant_ocurrencia += 1
    return ((cant_ocurrencia + k)/(cant_observaciones + k*2))

"""
INPUT: array de strings, int k, "spam" o "ham", array palabras de ham, array palabras de spam, int palabras totales, matriz de etiqueta con frases
"""
def propabilidadTotal(mensaje, k, objetivo, tipo_ham, tipo_spam, palabras_totales, grupo):
    parte1 =  probabilidadOracion(mensaje, k, tipo_spam, palabras_totales)*probabilidadMain(grupo, "spam", k)
    parte2 =  probabilidadOracion(mensaje, k, tipo_ham, palabras_totales)*probabilidadMain(grupo, "ham", k)
    #print(parte1, parte2)
    if(parte1==0.0): parte1 = 0.0000000001
    if(parte2==0.0): parte2 = 0.0000000001
    
    if (objetivo=="spam"): return ((parte1)/(parte1 + parte2))
    elif(objetivo=="ham"): return ((parte2)/(parte2 + parte1))
    
def readEntryFile(file_name, sanit=True, log=False, split=False):
    matriz = []
    data = [sanitizar(line.strip()) for line in open(file_name, 'r')]
    for i in range(len(data)):
        columna = []
        if(split): phrase = data[i].split(" ")
        else: phrase = data[i]
        columna.append(phrase)
        matriz.append(columna)
    
    if (log):
        for j in range(len(data)):
            print(matriz[j])
        print("\n")
    return matriz

def generateOutputMatrix(input_matrix, i_actual, ham_words, spam_words, len_total_words_training, training_group, log=False ):
    salida = []
    for i in range(len(input_matrix)):
        tupla_salida = []
        tupla = input_matrix[i]
        
        if(len(tupla)==2): phrase = sanitizar(tupla[1])
        elif(len(tupla)==1): phrase = sanitizar(tupla[0])
        phrase_words = phrase.split(" ")
        
        if(log): print ("i: ", i_actual," iter: ", i, ": ", phrase)
        
        prob_spam = propabilidadTotal(phrase_words, i_actual, "spam", ham_words, spam_words, len_total_words_training, training_group)
        prob_ham = propabilidadTotal(phrase_words, i_actual, "ham", ham_words, spam_words, len_total_words_training, training_group) 
        predicted = ""
        if(prob_spam > prob_ham): predicted = "spam"
        elif(prob_spam <= prob_ham): predicted = "ham"
        
        tupla_salida.append(predicted)
        tupla_salida.append(phrase)
        salida.append(tupla_salida)
    return salida
            
def getAccuracy(matrix_to_evaluate, base_matrix, log=False):
    #if(len(matrix_to_evaluate)!=len(base_matrix)):
    #    print("MATRICES DIFERENTES LEN")
    #else:
        aciertos = 0
        for i in range(len(matrix_to_evaluate)):
            tupla_to_evaluate = matrix_to_evaluate[i]
            tupla_base = base_matrix[i]         
            if (log): print(tupla_to_evaluate[0], tupla_base[0])
            if(tupla_to_evaluate[0]==tupla_base[0]):
                aciertos += 1
        return (aciertos/len(matrix_to_evaluate))
 

def writeOutput(matrix, name):
    file = open(name, "w")
    for i in range(len(matrix)):
        tupla = matrix[i]
        file.write(str(tupla[0])+" \t"+str(tupla[1])+"\n")  
    file.close()