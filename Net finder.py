# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:16:30 2021

@author: murat
"""
"""
print("You can either type SUM or SUBSTRACT or END with floats\n When the list ends enter 0 to execute summing or subtraction")

c = 1
c1 = 0
c2 = 0
b = "nde"
k = -1
k1 = -1

a = input(" add or sub ? : ")

while b != "end" :
 if a == "add" :
  while  (c != 0):  
   c = float(input("Enter your values: "))
   c1 += c
   k += 1
  b = input("End? : ")
  if b == "end":
      break
  a = input(" add or sub or ? : ")
  c = 1
  if a == "sub" :
   while  (c != 0):  
    c = float(input("Enter your values: "))
    c2 -= c
    k1 += 1
  b = input("End? : ")
m = c1 + c2
print(f" {k} items added which resulted {c1}. {k1} items substracted with the net {c2}. Net is {m}")

f = input("Bye?")
"""
def standart_deviation(num_set):
    if  num_set[1] != True:
        return print("Invalid! Only one element has no deviation!!")
    deviation = 0.0
    median = sum(num_set)/len(num_set)
    for f in range (len(num_set)):
        deviation += (num_set[f] - median)**2
    variance = deviation / float((len(num_set)-1))
    standart = variance**0.5
    return standart,num_set

def add():
    b = []
    m = 0
    a = input("Your value:")
    while a != "":
         b.append(a)
         a = input("Your value:")
    for e in range(len(b)):
        b[e] = float(b[e])
        m += b[e]
    return m
def sub():
    b = []
    m = 0
    a = input("Your value:")
    while a != "":
         b.append(a)
         a = input("Your value:")
    for e in range(len(b)):
         b[e] = float(b[e])
         m -= b[e]
    return m
b = dict()
j = 1
f = 1
dic = 0
print("To add a plus group type 'add'.Conversly to add a negative group type 'sub' (To store use 'yes' and 'no') \n You can view all groups by typing 'list'. You can sum all the groups by typing 'result'.")
while True:
    a = input("Do you want to add or substract the values? \n")
    if a == "sub":
        k = sub()
        j += 1
        print("Do you want to store the Summation Set?")
        g = input()
        if g == "yes":
         ch = input("Do you want to name it? ")
         if ch == "no":
             b["sub"+str(j)] = k
             dic += k
         elif ch == "yes":
             ch1 = input("What should its name be? ")
             b[ch1] = k
             dic += k
         else:
             print("Invalid command")

    elif a == "add":
            k1 = add()
            f += 1
            print("Do you want to store the Summation?")
            g1 = input()
            if g1 == "yes":
                ch2 = input("Do you want to name it? ")
                if ch2 == "no":
                    b["sub"+str(j)] = k1
                    dic += k1
                elif ch2 == "yes":
                    ch3 = input("What should its name be? ")
                    b[ch3] = k1
                    dic += k1
                else:
                    print("Invalid command")
    elif a == "result":
        print("The total is " + str(dic))
    elif a == "list":
     print(b)
    elif a == "dev":
     set1 = input("Which set do you want to finds its standart deviation? ")
     if set1 in b:
        print(standart_deviation(b[set1]))
     else:
        print("You can only use 'sub','add','result','dev' and 'list'")
    