# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:33:08 2018

@author: aa-ol
"""

import functions as funct
import logic

def main ():
    best_k, best_accuracy = 0, 0.0
    # Obtaining and growing vareables to perform training and tests
    # The data is stored in a matrix to obtain the information separated by line and labeled
    matrix = funct.getText("corpus.txt", False)
    
    # It is decided to have a sample of 80% and 50% of the data that was previously obtained
    training = funct.sampleF(matrix, .8)
    test = funct.sampleF(matrix, .5)
    
    # Cross validation is obtained
    cross_validation = funct.sampleF(matrix, 1)
    
    # The data is classified according to the label and the number of words per label is calculated
    spam, ham = funct.classify(training)
    spam_words = funct.uniqueF(spam)
    ham_words = funct.uniqueF(ham)
    
    # The total number of words used for training is calculated 
    column = []
    for i in range(len(matrix)):
        label = training[i]
        column.append(label[1])
    total_words_training = funct.uniqueF(column)
  
    
    # Initialize test
    
    for i in range(1,10):
        salida_cross = logic.generateOutputMatrix(cross_validation, i, ham_words, spam_words, len(total_words_training), training)
        accuracy = logic.getAccuracy(salida_cross, cross_validation)
        if (accuracy > best_accuracy): best_accuracy, best_k = accuracy, i
    print("\nCROSS VALIADTION: Best K: ", best_k, " | Accuracy: ", best_accuracy)
    
    #--Test Phase---
    salida_test = logic.generateOutputMatrix(test, best_k, ham_words, spam_words, len(total_words_training), training)
    test_acc = logic.getAccuracy(salida_test, test)
    print("\nTEST: Best K: ", best_k,   " | Accuracy: ", test_acc, "\n")
    
    #--Input Phase---
    input_file = funct.getText("prueba.txt",True)
    salida_input = logic.generateOutputMatrix(input_file, best_k, ham_words, spam_words, len(total_words_training), training)
    funct.writeOutput(salida_input, "output.txt")
    

main()