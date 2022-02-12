# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:50:42 2022

@author: murat
"""
word = "TESTING"

def code(message,hardness):
    codex = ""
    noise ="wuowhfwbvdguyqfvuösmbvfbhs"
    message = str(message)
    noise = noise*(int(len(message)*(hardness)**1/2))
    a = []
    for i in range(0,len(noise)):
     a.append(noise[i])
    for i in range(0,len(message)):
     a[hardness*i] = message[i]
    for i in range(0,len(noise)):
     codex += a[i]
    return codex

def freq(word): # Finds the frequency of each letter
	B =[]
	for i in range(0,len(word),1):
 		B.append(str(word.count(word[i]))+ " " + word[i])
	print(set(B))
    
def tryHard(x): # Possible decipherer
 a = []
 for k in range(0,len(x)):
  for i in range(k,len(x)):
   y = ""
   #print("\n")
   for n in range(k,len(x),i+1):
    y += x[n]
   a.append(y)
 a = sorted(set(a),key=len,reverse=False)
 for i in a:
     if len(i) > 4:
         print(i)
         
#tryHard("Wuorhfibvtgueqf uöHmbefbrswe")

print(code(word,2)) # write your message to the first place and the seperation to the next
#tryHard(code(word,2))

"""
for i in range(0,len(findit("Deciphering",3)[3*i])
"""