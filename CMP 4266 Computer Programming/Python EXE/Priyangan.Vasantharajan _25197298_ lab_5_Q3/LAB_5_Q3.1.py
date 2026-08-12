# -*- coding: utf-8 -*-
"""
Spyder Editor

V_Priyangan 25197298
lab - 5
Q-3.1
"""
def create_list():
    return ["playstation", "xbox", "steam", "ios", "google play"]

def get_info(my_list):
    first = my_list[-5]
    second_last = my_list[-2]
    total_ele = len(my_list)
    return (first, second_last,total_ele)

def get_partial(my_list):
    return my_list[1:4]

def last_three (my_list):
    return my_list [-1:-4:-1]

def double_list (my_list):
    return (my_list + my_list)

def amend (my_list):
    new_list = my_list.copy()
    new_list[1] = "None"
    new_list.append("bye")
    return new_list
    
if __name__ == "__main__" : 
    test_list= create_list()
   
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))
    