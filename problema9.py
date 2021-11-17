# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:09:46 2021

@author: Maxim Durnea
"""

stop="stop"
x=1
a=set()
b=set()
elem_a=" "
print("dati elementele multimii \"a\":\ndaca doriti sa treceti la multimea \"b\",tastati \"stop\"")
while (elem_a!=stop):
  elem_a=input("\"{}\"".format(x))
  if (elem_a.isalpha()):
   a.add(elem_a.upper())
  elif elem_a==stop:
      print("STOP")
  else:
   print("Doar Litere!")
  x+=1
a.remove("STOP")
print(a)
elem_a=0
x=1
print("dati elementele multimii \"b\":\ndaca doriti sa va opriti,tastati \"stop\"")
while (elem_a!=stop):
  elem_a=input("\"{}\"".format(x))
  elem_a.upper()
  if (elem_a.isalpha()):
   b.add(elem_a.upper())
  elif elem_a==stop:
      print("STOP")
  else:
   print("Doar Litere! ")
  x+=1
b.remove("STOP")
print(b)
print("intersectia a cu b: ",a.intersection(b))
print("reuniunea a cu b",a.union(b))
print("diferenta a cu b",a.difference(b))
     