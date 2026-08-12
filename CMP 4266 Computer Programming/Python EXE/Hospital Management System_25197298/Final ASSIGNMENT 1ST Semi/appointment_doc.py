# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:08:41 2026

@author: Priyangan
"""

class Appointments:
    def __init__(self,doctor_id,patient_id, date):
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.date = date
        
                       
    def __str__(self):
        return ("Our Honorable Doctor  "+self.doctor_id +
            " is booked by our respectful patient " +
                self.patient_id + " on " + self.date +
                    ". Thank You.")
    