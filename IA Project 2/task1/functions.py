# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:34:01 2018

@author: aa-ol
"""

import random, re

# Function so that all the letters are lowercase
def sanitizer(string_input):
    return ((re.sub('[^A-Za-z0-9 \t]+', '', string_input)).lower())

# Function to write a txt file
def write(matrix, name):
    file = open(name, "w")
    for i in range(len(matrix)):
        Label = matrix[i]
        file.write(str(Label[0])+" \t"+str(Label[1])+"\n")  
    file.close()

# Function to open txt files and save them line by line
def getText(file_name, its_entry):
    matrix = []
    data = [sanitizer(line.strip()) for line in open(file_name, 'r', encoding="utf8")]
    
    for i in range (len(data)):
        line = []
        if (its_entry):
            phrase = data[i]
            line.append(phrase)
        else:
            x,y = data[i].split("\t")
            line.append(x)
            line.append(y)
        
        matrix.append(line)
    return matrix

# Function to separate the data by percentage and  obtain a sample
def sampleF(matrix, percentage):
    training_sample = []
    for _ in range (0, int((len (matrix))*percentage)):
        training_sample.append(matrix.pop(random.randrange(0, len(matrix))))
    return training_sample

# Function to classify what type of data is per line according to flag
def classify(matrix):
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
def uniqueF(array):
    unique = []
    for i in range(len(array)):
        phrase = array[i].split(" ")
        for word in phrase:
            if word not in unique:
                unique.append(word)
    return unique

 

