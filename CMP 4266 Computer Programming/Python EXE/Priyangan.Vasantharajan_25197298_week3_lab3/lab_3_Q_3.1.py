# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 05:13:52 2026

@author: Priyangan
"""
balance= 1000
amount=0


name=input("Enter your name?")
while True:
    print(':::::::menu:::::::')
    print('1.Make Deposit')
    print('2.Make a Withdrawal')
    print('3.Obtain a balance')
    print('4.Quit')

    choose=int(input("Enter the option?"))

    if choose == 1:
        amount=int(input('Enter your deposit value amount?'))
        balance=balance+amount
        print('Your new balance:', balance)
    
    elif choose == 2:
        amount=int(input('Enter your withdrawal value amount?'))
        if amount >balance:
            print('It is not possible to withdraw beyond the account balance')
        else:
           balance=balance-amount
           print('Your new balance:', balance)
    elif choose == 3:
        print("Your balance:", balance)
    elif choose == 4:
        print('The End, Thank you')
    break


