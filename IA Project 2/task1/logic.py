# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:34:43 2018

@author: aa-ol
"""
import functions as func

"""
INPUT: int K, string palabra, array tipo_palabra, int palabras_totales
"""
def laplaceSmoothingBasic(k, palabra, tipo_palabra, palabras_totales):
    res = 0.0
    cant_ocurrencia = 0.0
    cant_observaciones = len(tipo_palabra)
    for i in range(len(tipo_palabra)):
        if tipo_palabra[i]==palabra: cant_ocurrencia +=1
    res = (cant_ocurrencia+k)/(cant_observaciones+k*palabras_totales)
    return (res)

"""
INPUT: array string mensajes, int k, array tipo_palabra, int palabras_totales
"""
def probabilidadOracion(mensaje, k, tipo_palabra, palabras_totales):
    probabilidad = 1.0
    
    for i in range(len(mensaje)):
        laplace = laplaceSmoothingBasic(k, mensaje[i], tipo_palabra, palabras_totales)
        probabilidad =  probabilidad * laplace
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
    
    if(parte1==0.0): parte1 = 0.0000000001
    if(parte2==0.0): parte2 = 0.0000000001
    
    if (objetivo=="spam"): return ((parte1)/(parte1 + parte2))
    elif(objetivo=="ham"): return ((parte2)/(parte2 + parte1))
    


def generateOutputMatrix(input_matrix, i_actual, ham_words, spam_words, len_total_words_training, training_group):
    salida = []
    for i in range(len(input_matrix)):
        tupla_salida = []
        tupla = input_matrix[i]
        
        if(len(tupla)==2): phrase = func.sanitizer(tupla[1])
        elif(len(tupla)==1): phrase = func.sanitizer(tupla[0])
        phrase_words = phrase.split(" ")
        
        
        prob_spam = propabilidadTotal(phrase_words, i_actual, "spam", ham_words, spam_words, len_total_words_training, training_group)
        prob_ham = propabilidadTotal(phrase_words, i_actual, "ham", ham_words, spam_words, len_total_words_training, training_group) 
        predicted = ""
        if(prob_spam > prob_ham): predicted = "spam"
        elif(prob_spam <= prob_ham): predicted = "ham"
        
        tupla_salida.append(predicted)
        tupla_salida.append(phrase)
        salida.append(tupla_salida)
    return salida
            
def getAccuracy(matrix_to_evaluate, base_matrix):
        aciertos = 0
        for i in range(len(matrix_to_evaluate)):
            tupla_to_evaluate = matrix_to_evaluate[i]
            tupla_base = base_matrix[i]         
            if(tupla_to_evaluate[0]==tupla_base[0]):
                aciertos += 1
        return (aciertos/len(matrix_to_evaluate))