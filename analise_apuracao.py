#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 17:45:44 2022

@author: rodrigosferreira
"""

#coisas que precisarão ser analisadas

# Nome dos candidatos - ver se o DataFrame é diferente;
# URL no arquivo apuracao.py

import pandas as pd
import ast
#import matplotlib.pyplot as plt

def create_graph():
    data = pd.read_csv('apuracao.txt', sep=";", header=None)
    
    results = pd.DataFrame()
    
    for i in data.index:
        data[1][i] = ast.literal_eval(data[1][i])
    
        df = pd.DataFrame(
            [[
                ast.literal_eval(data[1][i]['LULA']),ast.literal_eval(data[1][i]['JAIR BOLSONARO'])
                ]], 
              columns=["LULA","JAIR BOLSONARO"],index=[data[0][i]])
        
        results = results.append(df)
    
    
    #Converting to Datetime
    
    results.index = pd.to_datetime(results.index)
    
    results.plot()

create_graph()
