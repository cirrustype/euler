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























