# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 10:11:39 2026

@author: Priyangan
"""

#for sqrt
import math

#input values
A = int(input('enter value for A:'))
B = int(input('enter value for B:'))
C = int(input('enter value for C:'))

print('A=',A, 'B=',B, 'C=',C)

#DISCRIMINANT 
d = math.sqrt(B*B - 4*A*C)

#ROOTS
root1 = (-B + d) / (2*A)
root2 = (-B - d) / (2*A)

#PRINT
print('root1=', root1)
print('root2=', root2)

