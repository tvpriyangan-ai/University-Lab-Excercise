# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 16:20:54 2026

@author: Priyangan
"""

def read_number():
    n1=int(input("enter your number:"))
    n2=int(input("enter your second number:"))
    op =str(input("enter your operator +, -, /, * :"))
    return n1,n2,op

def add_numbers(n1, n2):
    return n1+n2
    
def multiply_numbers(n1, n2):
    return n1*n2
    
def substract_numbers(n1, n2):
    return n1-n2
    
def divide_numbers(n1, n2):
    return n1/n2
    
def calculator():
    n1, n2, op =read_number()
    
    if op == "+":
        result= n1+n2
        print (n1+n2)
    elif op == "-":
        result = n1-n2
        print(f"{n1} - {n2} = {result}")
    elif op=="/":
        result = n1/n2
        print(f"{n1} / {n2} = {result}")
    elif op == "*":
        result = n1*n2
        print(f"{n1} * {n2} = {result}")
    else:
        print("Invalid Aritmetric Operator, Try Again")
calculator()


