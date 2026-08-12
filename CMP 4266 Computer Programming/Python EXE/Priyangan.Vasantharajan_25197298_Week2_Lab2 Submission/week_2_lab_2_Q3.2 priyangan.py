# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:49:53 2026

@author: Priyangan
"""

year = int(input("write a year which one you check?"))

if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
    print("leap year")
else:
    print("not a leap year")
    
    
    
