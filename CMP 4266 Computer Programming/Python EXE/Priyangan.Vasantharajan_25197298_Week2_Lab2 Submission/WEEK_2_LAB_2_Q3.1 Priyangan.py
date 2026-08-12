# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 09:30:23 2026

@author: Priyangan
"""


emp_name = input(float("Type your Name?"))
working_hours = float(input("Type your working hours per week?"))


hourly_wage = 22
standard_hours = 40
extra_pay = 1.5 * hourly_wage
extra_hours = working_hours - standard_hours
extra_pay = extra_hours * 1.5 * 22
standard_pay = 40 * hourly_wage
total_pay = standard_pay + extra_pay

if working_hours <= 40:
    print(working_hours * hourly_wage)
else:
    print(extra_pay + standard_pay)
    
    
    



