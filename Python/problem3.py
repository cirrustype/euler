# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:50:32 2021

@author: Hal
"""

# Austin Schenk
#Project Euler, Problem 3: largest prime factor. 

import numpy as np
import math


#def prime (n):
    
def factors(n):
    m = math.ceil(math.sqrt(n))
    seq = list(range(1, m+1))
    qes = list(reversed(seq))
    
    for i in qes:
        if n%i == 0:
            print(i)
        else:
            continue
    
    


print(math.sqrt(600851475143))


factors(600851475143)







def primes (n):

    i = 2
    factors = []
    while (i * i) <= n:
        if n % i :
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    
    largest = factors[len(factors) - 1]
    
    return largest



        
        
        
        
primes(600851475143)     
        
        










