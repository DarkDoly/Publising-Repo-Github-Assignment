# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 11:09:17 2024

@author: maxdu
"""

#mode

def mode(x):
    y = {}
    for a in x:
        y[a]=1
    else:
        y[a]+=1
    return [g for g,l in y.items() if l==max(y.values())]
print(mode([1,5,2,2,45,56,43,43,67,8,4,3,4,5,4,0,9,83,4,6657,5,1,1,2,4,43,2]))
    