# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:33:08 2018

@author: aa-ol
"""

import functions as fc

def main ():
    matriz = fc.getText("corpus.txt")
    training = fc.trainingSample(matriz, .8)
    test = fc.trainingSample(matriz, .5)
    cross_validation = fc.trainingSample(matriz, 1)
    
    print ("El tamaño de las oraciones con etiqueta es de :", str(len(matriz)))
    print ("Tamañ 0.8 de los datos es de:", str(int(len(matriz)*.8)), "\n")
    
    
    
main()