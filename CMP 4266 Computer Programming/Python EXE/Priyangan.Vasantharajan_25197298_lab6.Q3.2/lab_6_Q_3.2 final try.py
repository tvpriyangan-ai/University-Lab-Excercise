# -*- coding: utf-8 -*-

def view_contacts(contacts):
    i=1
    for name,num in contacts:
        print(i, name, num)
        i +=1
    
def add_contact(contacts):
    name = input("Enter contact Name:")
    num = input("Enter contact Number:")
    
    contact_file = (name, num)
    contacts.append( contact_file )
    
    print(f"{name} {num} has been added into the contact successfully")
    
def delete_contact(contacts):
    item_index = int(input("which number/position do you want to dlt:"))
    if 1 <= item_index <= len(contacts):
        name, num = contacts.pop(item_index-1)
        print(f"deleted successfully{item_index} {name} {num}")
    else:
        print("Invalid")
        
        
def main():
    contacts = [("stish", "123"), ("rita", "321")]
    while True:
       print( "~~~~Select an Operation~~~~")
       print( "v.View Contacts")
       print( "a.Add contacts")
       print( "d.delete contacts")
       print( "q.Quit")

       choose=input("Enter the option : (v/a/d/q) ?")

       if choose == "v":
           view_contacts(contacts)
        
       elif choose == "a":
           add_contact(contacts)
        
       elif choose == "d":
           delete_contact(contacts)
       
       elif choose == "q":
           print("quit")
       
           break
       else:
           print("Invalid")

if __name__ == "__main__":
    main()
    