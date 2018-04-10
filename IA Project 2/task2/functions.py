# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 09:27:23 2018

@author: aa-ol
"""

def redFile (file_name):
    matrix =[]
    data = clean([line for line in open(filename, 'r')])
    for i in range (len(data)):
        this = []
        y, x = line.split(",")
        this.append(y)
        this.append(x)
        matrix.append(this)
    return matrix

def cleanData (string_input):
    return ((re.sub('[0-9]+', '', string_input)).lower()) 