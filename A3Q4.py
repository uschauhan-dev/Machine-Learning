#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:43:56 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:47:35 2024

@author: Student
"""

import numpy as np
from numpy import linalg as LA

arr_1 = np.array([[1, 2], [3, 4]]) 
arr_2 = np.array([[2, 4], [6, 9]])

dot_prod=np.dot(arr_1,arr_2)
print("Dot Product: ",dot_prod)

print("Eigen values and Eigen vectors of 1st matrix: ")

eigen_values, eigen_vectors = LA.eig(arr_1)
print("Eigen values are: ", eigen_values)
print("Eigen vectors are: ",eigen_vectors)

print("determinant of arr1")
print(LA.det(arr_1))
print("determinant of arr2")
print(LA.det(arr_2))

print("Inverse of matrix 1:")
print(LA.inv(arr_1))
print("Inverse of matrix 2:")
print(LA.inv(arr_2))