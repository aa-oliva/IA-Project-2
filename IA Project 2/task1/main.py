# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:33:08 2018

@author: aa-ol
"""

import functions as funct

def main ():
    # Obtaining and growing vareables to perform training and tests
    # The data is stored in a matrix to obtain the information separated by line and labeled
    matrix = funct.getText("corpus.txt")
    
    # It is decided to have a sample of 80% and 50% of the data that was previously obtained
    training = funct.trainingSample(matrix, .8)
    test = funct.trainingSample(matrix, .5)
    
    # Cross validation is obtained
    cross_validation = funct.trainingSample(matrix, 1)
    
    # The data is classified according to the label and the number of words per label is calculated
    spam, ham = funct.classifyMessages(training)
    spam_words = funct.getUniqueWords(spam)
    ham_words = funct.getUniqueWords(ham)
    
    # The total number of words used for training is calculated 
    total_words_training = funct.getUniqueWords(funct.getColumna(training, 1))
    
    # The results are printed  
    print ("El tamaño de las oraciones con etiqueta es de :", str(len(matrix)))
    print ("Tamañ 0.8 de los datos es de:", str(int(len(matrix)*.8)), "\n")
    
    # Initialize test
    best_i, best_accuracy = 0, 0.0
    
    for i in range(1,10):
        salida_cross = funct.generateOutputMatrix(cross_validation, i, ham_words, spam_words, len(total_words_training), training, True)
        accuracy = funct.getAccuracy(salida_cross, cross_validation)
        if (accuracy > best_accuracy): best_accuracy, best_i = accuracy, i
    print("\nCROSS VALIADTION: Mejor i y accuracy: ", best_i, ": ", best_accuracy)
    
    #--Test Phase---
    salida_test = funct.generateOutputMatrix(test, best_i, ham_words, spam_words, len(total_words_training), training, True)
    test_acc = funct.getAccuracy(salida_test, test)
    print("\nTEST: i y accuracy: ", best_i, ": ", test_acc, "\n")
    
    #--Input Phase---
    input_file = funct.readEntryFile("prueba.txt", True, False, False)
    salida_input = funct.generateOutputMatrix(input_file, best_i, ham_words, spam_words, len(total_words_training), training, True)
    funct.writeOutput(salida_input, "output.txt")
    
main()