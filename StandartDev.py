# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:01:09 2021
@author: murat
"""
def isfloat(x):
    if "." in x:
        return True
    elif x == "":
        return False
    elif int(x) != None:
        return True
    else:
        return False



def the_number_list():
    a = []
    k = 0
    while k != "":
        k = input()
        if isfloat(k) :
            a.append(float(k)) # += splits the integers!!!
        elif k == "" :
         return a
        elif isfloat(k) == False :
         print(f"{k} is not a number!")
    return a

def standart_deviation(num_set):
    if  len(num_set) == 1:
        return "Invalid! Only one element has no deviation!!"
    deviation = 0.0
    median = float(sum(num_set)/len(num_set))
    for f in range (len(num_set)):
        deviation += (num_set[f] - median)**2
    variance = deviation / float((len(num_set)-1))
    standart = variance**0.5
    return standart,num_set


while True:
 print("Here we calculate standart deviation\n" + "Enter the numbers please:")
 print(standart_deviation(the_number_list()))
 print("\n")
 