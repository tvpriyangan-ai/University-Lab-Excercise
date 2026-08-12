# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 09:09:39 2026

@author: Priyangan
"""

def create_list():
    return ["playstation", "xbox", "steam", "ios", "google play"]

def get_info(my_list):
    the_first_element = my_list[0]
    the_second_last_element = my_list[-2]
    number_of_element=len(my_list)
    
    return the_first_element, the_second_last_element, number_of_element

def get_partial(my_list):
    return my_list [1:4]

def get_last_three(my_list):
    new_list= my_list.copy()
    new_list.reverse()
    return new_list[:3]


def double_list(my_list):
    return (my_list + my_list)

def amend(my_list):
    new_list= my_list.copy()
    new_list[1]="none"
    new_list.append("bye")
    return new_list

    

if __name__ =="__main__":
    test_list=create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))
    
