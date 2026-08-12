# -*- coding: utf-8 -*-
"""
@author: Priyangan
"""


def get_data():
    h= int(input("Provide the number of houses with 0 occupancy:"))
    h1= int(input("Provide the number of houses with 1 occupancy:"))
    h2= int(input("Provide the number of houses with 2 occupancy:"))
    h3= int(input("Provide the number of houses with 3 occupancy:"))
    h4= int(input("Provide the number of houses with 4 occupancy:"))
    h5= int(input("Provide the number of houses with 5 occupancy:"))
    h6= int(input("Provide the number of houses with 6 occupancy:"))
    h6plus= int(input("Provide the number of houses with 6+ occupancy:"))

    return h,h1,h2,h3,h4,h5,h6,h6plus


def cal_percentage(h,h1,h2,h3,h4,h5,h6,h6plus):
    
    total= h+h1+h2+h3+h4+h5+h6+h6plus
    
    per_value_0= (h/total)*100
    per_value1= (h1/total)*100
    per_value2= (h2/total)*100
    per_value3= (h3/total)*100
    per_value4= (h4/total)*100
    per_value5= (h5/total)*100
    per_value6= (h6/total)*100
    per_value6plus= (h6plus/total)*100
     
    return per_value_0,per_value1,per_value2,per_value3,per_value4,per_value5,per_value6,per_value6plus
 
    
def display_result(h,h1,h2,h3,h4,h5,h6,h6plus,per_value_0,per_value1,per_value2,per_value3,per_value4,per_value5,per_value6,per_value6plus):
   print("\nOccupants:       0       1       2       3       4       5       6       6+")
   print(f"No.of.Houses:    {h}        {h1}     {h2}      {h3}    {h4}        {h5}       {h6}       {h6plus}")
   print(f"Percentage:    {per_value_0:.2f}      {per_value1:.2f}    {per_value2:.2f}    {per_value3:.2f}     {per_value4:.2f}    {per_value5:.2f}    {per_value6:.2f}    {per_value6plus:.2f}") 



if __name__=="__main__":
    h,h1,h2,h3,h4,h5,h6,h6plus = get_data()
    per_value_0,per_value1,per_value2,per_value3,per_value4,per_value5,per_value6,per_value6plus= cal_percentage(h,h1,h2,h3,h4,h5,h6,h6plus)
    display_result(h,h1,h2,h3,h4,h5,h6,h6plus,per_value_0,per_value1,per_value2,per_value3,per_value4,per_value5,per_value6,per_value6plus)
    
    
    
    
    
