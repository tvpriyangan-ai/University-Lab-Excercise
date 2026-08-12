# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 09:14:09 2026

@author: Priyangan
"""

class Patients:
    def __init__(self, patient_name, patient_age,patient_id):
        
        self.patient_name = patient_name
        self.patient_age= patient_age
        self.patient_id = patient_id
        self.prescriptions = []
                
    def get_details(self):
        return (self.patient_name, self.patient_age, self.patient_id)
    
    def add_prescriptions(self,medicine_details):
        self.prescriptions.append(medicine_details)
   
    def __str__(self):
        return "The patient's Name is "+self.patient_name+\
            " and his/her age is "+ self.patient_age+\
                " and also ID Number is "+self.patient_id