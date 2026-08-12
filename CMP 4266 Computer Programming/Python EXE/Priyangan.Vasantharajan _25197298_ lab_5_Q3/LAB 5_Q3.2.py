# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
guests=[]


while True:
    print("____Options____") 
    print("A.Add a guest")
    print("R.Remove a guest")
    print("P.Print guest list")
    print("Q.Quit the program")
    
    enter_option=input("Enter your option in Upper case Letter:")
       
    if enter_option == "A":
       guest_name=input("Enter your guest name:")
       guests.append(guest_name)
       print("{} has been added to the list as a guest".format(guest_name))
    
    elif  enter_option == "R":
        guest_name=input("Enter your guest name which will be removed:")
        if guest_name in guests:
            guests.remove(guest_name)
            print("{} has been removed from the list".format(guest_name))
        else:
            print("this guest name is not on the list.")
    
    elif enter_option == "P":
        guests.sort()
        print("Guest List:", guests)
        
    elif enter_option == "Q":
        print("Goodbye! See you in the party!") 
        
    else:
        print("Invalid choice")  
        break