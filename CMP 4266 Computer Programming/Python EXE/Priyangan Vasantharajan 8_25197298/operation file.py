# -*- coding: utf-8 -*-
"""


@author: Priyangan
"""
from L8_library import BankAccount


acc1=BankAccount(1,100)
acc2=BankAccount(2,100)

accounts=[acc1, acc2]


for acc in accounts:
    acc.withdraw(40)
    
for acc in accounts:
    print(acc.get_account(),acc.get_balance())
    
for acc in accounts:
    acc.deposit(20)
    
for acc in accounts:
    print(acc.get_account(), acc.get_balance())
    
acc2.transfer(20,acc1)

for acc in accounts:
    print(acc.get_account(), acc.get_balance())