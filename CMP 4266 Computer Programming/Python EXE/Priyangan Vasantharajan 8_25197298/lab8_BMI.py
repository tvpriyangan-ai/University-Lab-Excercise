# -*- coding: utf-8 -*-
"""


@author: Priyangan
"""

class BMI:
    
    def __init__(self):
        self.__weight=0.0
        self.__height=0.0
        
    def set_weight(self, w):
        self.__weight=w
              
    def set_height(self,h):
        self.__height=h
       
    def __cal_BMI(self):
        if self.__height==0:
            return 0
        
        return self.__weight/ (self.__height**2)
    
    
    def display_BMI(self):
        final_BMI=self.__cal_BMI()
        print(F"Your BMI is {final_BMI:.2f}")

bmi=BMI()
bmi.set_weight(68)
bmi.set_height(1.78)
bmi.display_BMI()
