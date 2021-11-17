# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:20:03 2021

@author: Durnea Maxim
"""
stop="stop"
x=1
a=set()
b=set()
elem_a=" "
print("dati elementele multimii \"a\":\ndaca doriti sa treceti la multimea \"b\",tastati \"stop\"")
while (elem_a!=stop):
  elem_a=input("\"{}\"".format(x))
  if elem_a.isdigit():
   a.add(elem_a.upper())
  elif elem_a==stop:
      print("STOP")
  else:
   print("acesta nu este un numar!")
  x+=1
print(a)
elem_a=0
x=1
print("dati elementele multimii \"b\":\ndaca doriti sa va opriti,tastati \"stop\"")
while (elem_a!=stop):
  elem_a=input("\"{}\"".format(x))
  elem_a.upper()
  if elem_a.isdigit():
   b.add(elem_a.upper())
  elif elem_a==stop:
      print("STOP")
  else:
   print("acesta nu este un numar! ")
  x+=1
print(b)
print("intersectia a cu b: ",a.intersection(b))
print("reuniunea a cu b",a.union(b))
print("diferenta a cu b",a.difference(b))
print("diferenta b cu a",b.difference(a))
     

