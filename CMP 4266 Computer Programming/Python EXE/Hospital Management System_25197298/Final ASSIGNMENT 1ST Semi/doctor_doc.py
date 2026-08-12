# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:05:33 2026

@author: Priyangan
"""

class Doctors:
    def __init__(self,doctor_name, doctor_id, doctor_spe):
        self.doctor_name = doctor_name
        self.doctor_spe=doctor_spe
        self.doctor_id=doctor_id
     
    def __str__(self):
        return self.doctor_name + self.doctor_id + " who is specialist for " + self.doctor_spe