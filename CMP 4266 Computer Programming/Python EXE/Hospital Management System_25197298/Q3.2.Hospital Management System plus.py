# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:00:53 2026

@author: Priyangan
"""

class Hospital:
    def __init__(self):
        self.doctors_details = []
        self.patients_details = []
        self.appointments_details = []
    
    def add_patient(self,patient):
        self.patients_details.append(patient)
        
    def add_doctor(self,doctor):
        self.doctors_details.append(doctor)
        
    def view_patient(self):
        for particular_patient in self.patients_details:
            print(particular_patient)
    
    def book_appointment(self,patient,doctor,date):
       
        if self.doctor_available_checkup(doctor,date):
            register = Appointments_details(doctor,patient,date)
            self.appointments_details.append(register)
            print("Successfully Appointment Booked")
        else:
            print("Sorry! Doctor Not Available, Try to another Time please")
          
    def cancel_appointment(self,patient):
        for particular_patient_name in self.appointments_details:
            if particular_patient_name == patient:
                self.appointments_details.remove(particular_patient_name)
                print("Successfully Cancelled your Appoinment, Thank you")
                
    def find_patient(self,patient_id):
        for particular_patient in self.patients_details:
            if particular_patient == patient_id:
                return particular_patient
     
    def doctor_available_checkup(self, doctor,date):
        for particular_detail in self.appointments_details:
            if particular_detail.doctor == doctor and \
                particular_detail.date == date:
                return False
                print("Sorry, already Doctor Booked by someone," \
                      "Doctor Not available")   
            else:
                print("Good Luck, Doctor available so you can Book")
        return True
        
   
    def view_all_hospital_details(self):
        print("You can see All of our Hospital management system's details")
        
        print("1.Patients:")
        for patient_x in self.patients_details:
            print(patient_x)
        
        print("2.Doctors:")
        for doctor_x in self.doctors_details:
            print(doctor_x)
        
        print("3.Appointments:")
        for appointment_x in self.appointments_details:
            print(appointment_x)

    
class Doctors_details:
    def __init__(self,doctor_name, specialist):
        self.doctor_name = doctor_name
        self.specialist = specialist
     
    def __str__(self):
        return self.doctor_name + " who is specialist for " + self.specialist
           
 
                 
        
class Patients_details:
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
  


    
    
class Appointments_details:
    def __init__(self,doctor,patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.fee = 100
                       
    def __str__(self):
        return "Our Honorable Doctor  "+self.doctor.doctor_name +\
            " is booked by our respectful patient " +\
                self.patient.patient_name + " on " + self.date +\
                    ". Thank You."
    



    
hospital=Hospital()

p1=Patients_details("Priyan", "25", "25197298")
d1=Doctors_details("Kurtiz", "Neurology")

hospital.add_patient(p1)
hospital.add_doctor(d1)



    
    
hospital.book_appointment(p1,d1,"15/05/2026")
for particular_name in hospital.appointments_details:
    print(particular_name)
   

hospital.doctor_available_checkup(d1, "16/05/2026")
    
    
hospital.view_all_hospital_details()
    
    
    
    
    


