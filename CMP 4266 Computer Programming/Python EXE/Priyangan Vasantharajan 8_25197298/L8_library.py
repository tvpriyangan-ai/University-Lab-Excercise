# -*- coding: utf-8 -*-
"""

@author: Priyangan
"""

class BankAccount:
    def __init__(self,acc_number,balance=0.0):
        self.acc_number=acc_number
        self.balance=balance
        
    def get_account(self):
        return self.acc_number
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw (self,amount):
        if amount<=self.balance:
            self.balance-=amount
            
        else:
            print("Invalid")
            
    def transfer (self,amount,acc):
        
        if amount<=self.balance:
            self.balance-=amount
            acc.deposit(amount)
            
        else:
            print("invalid Transaction")