#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:42:17 2024

@author: Uday
"""

import numpy as np
arr_1= np.array([1,2,3,4])
arr_2=np.array([2,4,6,8])

add_res=np.add(arr_1, arr_2)
print("addition is: ",add_res)

print(np.subtract(arr_1,arr_2))
print(np.multiply(arr_1,arr_2))
print(np.divide(arr_1,arr_2))

print()
arr_3=np.random.randint(0,100,size=(3,4))
print(arr_3)

print()
print(np.exp(arr_1)) #e raised to the power of the specific number
print(np.log(arr_1))


arr_4=np.array([1.2,2.5,5.6,3.4])

print(np.ceil(arr_4))
print(np.floor(arr_4))