# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:16:08 2017

@author: Till Langbein
"""

import numpy as np

def sharpe_ratio(rp:float, rf:float, sdp:float)->float:
    return (rp - rf) / sdp

def avg(p:list)->float:
    temp = 0
    for x in p:
        temp += x
    return temp / len(p)

def standard_deviation1(p:list)->float:
    mean = avg(p)
    result = []
    for i in p:
        result.append((i - mean) ** 2)
    return (avg(result)) ** 0.5

def standard_deviation2(p:list)->float:
    n = len(p)
    mean = sum(p) / n
    result = ((i - mean) ** 2 for i in p)
    return (sum(result) / n) ** 0.5

def standard_deviation3(p:list)->float:
    return np.array(p).std()
    
    
if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 8, 7, 9]
    print(standard_deviation1(a))
    print(standard_deviation2(a))
    print(standard_deviation3(a))
