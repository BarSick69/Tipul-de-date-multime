# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:21:39 2021

@author: User
"""
import itertools
a=set(["A","B","C","D"])
for i in range(1,len(a)+1):
    for result in itertools.combinations(a,i):
        print(result,end=";")
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
b=set([1,2,3,4])
for x in range(1,len(a)+1):
    for result1 in itertools.combinations(b,x):
        print(result1,end=";")