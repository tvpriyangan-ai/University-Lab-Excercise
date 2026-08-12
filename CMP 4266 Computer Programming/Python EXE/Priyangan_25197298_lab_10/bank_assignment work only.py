class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        self.__cID=cID
        self.__first_name=first_name
        self.__second_name=second_name
        self.__address=address
        self.__balance=balance
        
    def get_cID(self):
        return self.__cID
    
    def set_cID(self, c_id):
        self.__cID=c_id
        
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self,  f_name):
        self.__first_name=f_name 
        
    def get_second_name(self):
        return self.__second_name 
    
    def set_second_name(self, s_name):
        self.__second_name=s_name 
        
    def get_address(self):
        return self.__address
    
    def set_address(self, addObj):
        self.__address =addObj
        
    def get_balance(self):
        return self.__balance
   
    def set_balance(self, value):
        self.__balance = value

    def deposite(self,value):
        self.__balance+=value

    def withdraw(self,value):
        self.__balance-=value

    def check_balnce(self):
        return self.__balance 

    

class Address:
    def __init__(self, number, street, town, post_code):
        self.__number=number
        self.__street=street
        self.__town=town
        self.__post_code=post_code
  
    def get_number(self):
        return self.__number
  
    def set_number(self, value):
        self.__number = value

  
    def get_street(self):
        return self.__street
    
    def set_street(self, value):
        self.__street = value

 
    def get_town(self):
        return self.__town
 
    def set_town(self, value):
        self.__town = value

  
    def get_post_code(self):
        return self.__post_code
    
    def set_post_code(self, value):
        self.__post_code = value

    def change_address(self,new_address):
        self.number = new_address.get_number()
        self.street = new_address.get_street()
        self.town = new_address.get_town()
        self.post_code= new_address.get_post_code()

    def __str__(self):
        return f"{self.__number},{self.__street},{self.__town},{self.__post_code}"

def new_customer():

    cid= int(input("Enter customer id number: "))
    f_name= input( "Enter first name: ")
    s_name= input("Enter second name: ")
    adres = input("Enter address (number, street, town, postCode): ")
    
    while len(adres.split(',')) != 4:
        adres = input( "Please re-enter address (number, street, town, postCode): ")
    number, street,town,postcode = adres.split(',')
    print(number, street,town,postcode)
    
    balance = float(input( "Enter balance: "))
    
    address_details= Address(number, street,town,postcode)
    customer_details=Customer(cid,f_name,s_name,address_details,balance)
    return customer_details

    

c = Customer('12A','Anna','Duka', Address(42,'Curzon Street','Birmingham', 'B4 2SU'),888)


def save_cRecords(lst):
    try:
        file=open("data_file", "w")
        for customer_details in lst:
            address_info=customer_details.get_address()
            file.write (f"{customer_details.get_cID()},{customer_details.get_first_name()},{customer_details.get_second_name()},{ address_info.get_number()},{ address_info.get_street()},{ address_info.get_town()},{ address_info.get_post_code()},{customer_details.get_balance()}\n") 
        file.close()
        return True
    except:
        return False

c1 = Customer('12A','Rea','Koci',Address('42','Curzon Street','Birmingham', 'B4 2SU'),888)
c2 = Customer('11A','Liora','Koci',Address('42b','Curzon Street2','Birmingham2', 'B4 2SU'),33)

save_cRecords([c1,c2])

def read_customerRecords(data_file):
    lst =  []
    
    try:
        file = open(data_file, "r")
        
        for line in file: 
            
            line=line.strip()
            
            fields = line.split(",")
            
            address_details = Address (str(fields[3]),str(fields[4]),str(fields[5]), 
                                        str(fields[6]))
            
            
            customer_details = Customer( fields[0] ,str(fields[1]) , 
                                        str(fields[2]),address_details, 
                                        (fields[7]))
            
            lst.append(customer_details)
        
        file.close()
        return lst
            
    except FileNotFoundError:
        print("Sorry, File Not Found! Please check and try again")
        
        
        return []
        
            
print(read_customerRecords('client_list.txt'))



