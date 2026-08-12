# -*- coding: utf-8 -*-
"""
Spyder Editor

This is Lab_1 Exercise script file.

#Lab 1 Exercise
#Calculate sum, average and sum of cubes
"""
#input values (decimals and integer also acceptable here,float is flexible)
a = float(input('enter value for a:'))
b = float(input('enter value for b:'))
c = float(input('enter value for c:'))

#calculate sum
tot = a + b + c

#calculate average
average = tot / 3

#calculate sum of cubes
sum_of_cubes = a**3 + b**3 + c**3

#print results
print('sum = ', tot)
print('average =', average)
print('sum_of_cubes = ', sum_of_cubes)
