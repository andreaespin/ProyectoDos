# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:14:16 2018

@author: usuario
"""

import re
from numpy import linalg as LA
import numpy as np

cachedStopWords= stopwords.words('spanish')

main_dir='D:/Mineria de datos/Codigo/dm.txt'

with open(main_dir) as content_file:
    text=content_file.read()
text=text.lower()
words=re.findall('[a-záéíóúñ]+',text)
Eliminado=set(words)
Eliminado=list(Eliminado)

with open(main_dir,"r") as ins:
    lines=[]
    for line in ins:
        lines.append(line.lower())
        
wordVector=[]
for eachline in lines:
    Vector=[]
    for Counts in Eliminado:
        Vector.append(eachline.count(Counts))
    wordVector.append(Vector)
print(len(wordVector))
        
for x in wordVector: 
    suma_columna = 0
    for y in wordVector:
        suma_columna = suma_columna +  wordVector[y][x]
        if (suma_columna > 0):
            vectorl=[]
            vectorl.append(suma_columna.count)
            print(vectorl)
    

    
   
    
