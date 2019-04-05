#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:39:12 2018

@author: jebcollins
"""



import numpy



def is_prime(nn):
    prime_flag = True
    for ii in range(2,nn):
        if(nn % ii == 0):
            prime_flag = False
            break
        
    return prime_flag




for nn in range(3, 1000000):
    if is_prime(nn) or nn % 2 == 0:
        continue
    
    mm = 1
    counterexample = True
    while nn - 2*(mm**2) >= 0:
        if is_prime(nn - 2*(mm**2)):
            counterexample = False
            break
        
        mm += 1
        
        
    if counterexample:
        print(nn)
        break