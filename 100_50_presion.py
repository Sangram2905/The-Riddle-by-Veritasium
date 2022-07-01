# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:36:51 2022

@author: sangramp
"""


import numpy as np
import pandas as pd
import random

# Created 3 list for the prisoner and Box as key and slip as Value 
prisionList,keyList,valList = list(range(0,100)),list(range(0,100)),list(range(0,100))

random.shuffle(prisionList)    
random.shuffle(keyList)
random.shuffle(valList)

box_dictionary = dict(zip(keyList,valList)) 

#Inintial entry


for p in range(len(prisionList)):
    i = prisionList[p]
    print("prisoner enter in room p_num: ",i)
    print(('{0},{1},{2},{3}'.format(i,"NA","NA","IN")),file=open("prisoner_result.csv", "a"))

    box_dictionary = dict(zip(keyList,valList)) # Reseting the room for each prisoner
    x = random.choice(box_dictionary)
    n = box_dictionary[x]

    for m in range(0,50):
        
        #print("prisoner {0} open box {1} contains value {2} : ".format(i,n,box_dictionary[n]))
        try:
            if i == box_dictionary[n] :
                print("prisoner {0} open box {1} contains value {2} : ".format(i,n,box_dictionary[n]))
                print(('{0},{1},{2},{3}'.format(i,n,box_dictionary[n],"OUT")),file=open("prisoner_result.csv", "a"))
                print("prisoner {0} out: ".format(i))
                break
            else:                        
                k = (list(box_dictionary.keys())[list(box_dictionary.values()).index(box_dictionary[n])])
                print("prisoner {0} open new box {1} contains value {2} ".format(i,k,box_dictionary[k]))
                print(('{0},{1},{2},{3}'.format(i,k,box_dictionary[k],"NA")),file=open("prisoner_result.csv", "a"))
                n = box_dictionary[k] # value insde the new box set to new box number
                box_dictionary.pop(k) # pop out the previus box
        except:
            print("Loop complete for prisoner: ",i)
            print(('{0},{1},{2},{3}'.format(i,"NA","NA","LoopEnd")),file=open("prisoner_result.csv", "a"))
            break
            
            
             
            

