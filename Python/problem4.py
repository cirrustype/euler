# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:36:13 2021

@author: Hal
"""


#A palindromic number reads the same both ways. The largest palindrome made 
#from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.



numbers = range(100, 999, 1)
numbers2 = range(100, 999, 1)

pals = []
for i in range(100,999):
    for j in range(100,999):
        p = i*j
        l= [int(x) for x in str(p)]
        if l == reversed(l):
            pals.append(pals)
        else:
            continue
        
        
        
            
        

print(pals)



print((999*999)-10000)
print(100*100)



import numpy as np

r = np.r_[10000:998001]

rr = np.asarray(reversed(r))

print(r)


rrr = []

for i in range(9,988001,10):
    rrr.append(r[i])
    
    
print(rrr)




threes = np.r_[100:1000]
threes2 = np.r_[100:1000]
l= [int(x) for x in str(threes[10])]
lr = l[::-1]
print(lr)
print(threes[10])


p = []
for i in threes:
    for j in threes2:
        p = threes[i]*threes2[j]
        
        pl = [int(x) for x in str(p)]
        plr = pl[::-1]
        if pl == plr:
            p.append(p)
        else:
            continue
        
        


