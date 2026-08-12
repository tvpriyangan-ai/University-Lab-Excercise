# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:09:51 2026

@author: Priyangan
"""
from appointment_doc import Appointments
from patient_doc import Patients
from doctor_doc import Doctors


class Hospital:
    
    def __init__(self):
        self.doctors_details = {}
        self.patients_details = {}
        self.appointments_details = []
    
  
       
    def add_patient(self):
        try:
            patient_id=input("Enter the Patient id: ")
            patient_name=input("Enter the patient_name: ")
            patient_age=(input("Enter the patient_age: "))
            
            if patient_id in self.patients_details:
                print("Sorry, Already Added")
            else:
                self.patients_details[patient_id] = Patients(patient_id,patient_name, patient_age)
                print("Successfully patient detail added")
                
        except ValueError:
            print("Age value is Invalid, Try again")
            
    def view_patients_details(self):
        if len(self.patients_details) == 0:
            print("Sorry, No any Patients details")
        else:
            for n in self.patients_details():
                print(n)

                    
            
            
            
            

    def add_doctor(self):
        doctor_id=input("Enter Doctor's ID:")
        doctor_name=input("Enter the Doctor's Name:")
        doctor_spe=input("Enter the Doctor's Specialist category:")
        
        self.doctors_details[doctor_id] = Doctors(doctor_id,doctor_name,doctor_spe) 
        if doctor_id in self.doctors_details:
            print("sorry, this ID already added")
            
        else:
            self. doctors_details[doctor_id] = Doctors(doctor_id, doctor_name, doctor_spe)
            print("Successfully Doctor id added")
            
            
    def view_doctors(self):
       
        if len(self.doctors_details)==0:
            print("Sorry, No Doctors details in here")    
        else:
            for n in self.doctors_details():
                print(n)
        
            
          
            
          
            

   
    def book_appointment(self):
        patient_id=input("Enter the patient_id:")
        doctor_id=input("Enter the Doctor_id:")
        date=input("Enter the date:")
        
                  
        if doctor_id in self.doctors_details and patient_id in self.patients_details:
            form = Appointments(doctor_id, patient_id, date)
            
            self.appointments_details.append(form)
            print("Successfully Appointment booked")
        else:
            print("Sorry, You can't Booked, Doctor not available")
            
            
    def cancel_appointment(self):
        patient_id=input(" Enter your patient_id:")
        for form in self.appointments_details:
            if form.patient_id == patient_id:
                self.appointments_details.remove(form)
                print("Successfully cancelled your appointment")
            else:
                print("Sorry, Invalid ID, Try Again")
        
                
    def view_appointments(self):
        if len(self.appointments_details) == 0:
            print("Sorry, No any applications in this program")
            
        else:
            for n in self.appointments_details:
                print(n)
      
            

                

        
def main():
    
    h=Hospital()
    
    
    
    while True:
        
        print("Main Menu")
        print("1.Add Patient")
        print("2.Add Doctor")
        print("3.View Patient")
        print("4.View Doctors")
        print("5.Book Appointment")
        print("6.Cancel Appointment")
        print("7.View All Appointments")
        print("8.EXIT")
        
        
        
        select=input("Enter your choice as a Number:")
        
        
        if select == "1":
            h.add_patient()
        elif select == "2":
            h.add_doctor()
        elif select == "3":
            h.view_patients_details()
        elif select == "4":
            h.view_doctors()
        elif select == "5":
            h.book_appointment()
        elif select == "6":
            h.cancel_appointment()
        elif select == "7":
            h.view_appointments()
        elif select == "8":
            break
        else:
            print("Invalid, Please select again")
          
            
          
if __name__ == "__main__":
    main()
            
            
            
        
                
            
        
            
    
                            