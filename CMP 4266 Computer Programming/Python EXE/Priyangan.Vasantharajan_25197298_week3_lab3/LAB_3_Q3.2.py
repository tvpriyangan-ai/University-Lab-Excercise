# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 06:24:59 2026

@author: 
"""

attempt=0


while attempt <5:
    password=str(input('ENTER YOUR PASSWORD:'))
    if password == 'test100':
        print("YOU'RE LOGGED IN")
        break
    else:
        print('WRONG PASSWORD!')
        attempt = attempt + 1
        
if attempt == 5:
     print("SORRY, YOU'VE REACHED THE MAXIMUM LOGON ATTEMPTS, TRY LATER")


            