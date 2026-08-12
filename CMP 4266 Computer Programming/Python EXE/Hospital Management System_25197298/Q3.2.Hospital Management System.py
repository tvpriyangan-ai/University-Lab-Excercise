# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:00:53 2026

@author: Priyangan
"""

class Hospital:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []
    
    def add_patient(self,patient):
        self.patients.append(patient)
        
    def add_doctor(self,doctor):
        self.doctors.append(doctor)
        
    def view_patient(self):
        for i in self.patients:
            print(i.name)
    
    def book_appointment(self,patient,doctor,date):
        form = Appointment(doctor,patient,date)
        self.appointments.append(form)
        if self.is_doctor_available(doctor,date):
            form = Appointment(doctor,patient,date)
            self.appointments.append(form)
            print("Appointment Booked")
        else:
            print("Doctor Not Available")
          
    def cancel_appointment(self,patient):
        for i in self.appointments:
            if i.patient == patient:
                self.appointments.remove(i)
                print("Cancelled")
                
    def find_patient(self,patient_id):
        for p in self.patients:
            if p.patient_id == patient_id:
                return p
     
    def is_doctor_available(self, doctor,date):
        for i in self.appointments:
            if i.doctor == doctor and i.date == date:
                return False    
        return True
    
    def view_all(self):
        print("Patients:")
        for p in self.patients:
            print(p)
        
        print("Doctors:")
        for d in self.doctors:
            print(d)
        
        print("Appointments")
        for a in self.appointments:
            print(a)

    
class Doctor:
    def __init__(self,name, specialization):
        self.name = name
        self.specilization = specialization
     
        def __str__(self):
         return f"name:{self.name}, specialization:{self.specialization}"    
           
 
                 
        
class Patient:
    def __init__(self, name, age,patient_id):
        
        self.name = name
        self.age= age
        self.patient_id = patient_id
        self.prescriptions = []
        
    def get_details(self):
        return (self.name, self.age, self.patient_id)
    
    def add_prescriptions(self,medicine):
        self.prescriptions.append(medicine)
   
    def __str__(self):
        return f"patient:{self.name}, age:{self.age}, patient_id:{self.patient_id}"
  


    
    
class Appointment:
    def __init__(self,doctor,patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.fee = 100
                       
    def __str__(self):
        return f"Dr. {self.doctor.name} booked with {self.patient.name} on {self.date}"
    



    
h=Hospital()
h.view_all()
p1=Patient("Priyan", "25", "25197298")
d1=Doctor("Kurtiz", "Neurology")

h.add_patient(p1)
h.add_doctor(d1)
print(p1)

h.book_appointment(p1,d1,"28/03/2026")
for form in h.appointments:
    print(form)
   
#print(h.find_patient("25197298"))
#or#
#result = h.find_patient("25197298")
#print(result)

if h.is_doctor_available(d1, "28/03/2026"):
    print("Doctor available")   
else:
    print("Doctor busy")
    
#h.cancel_appointment(p1)



