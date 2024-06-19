from scipy.linalg import det, inv
import numpy as np
A = np.array([[3,2,-1],
             [2,-4,7],
             [1,1,1]])

determinant_A = det(A)
inverse_A = inv(A)

print("Determinant of this matrix is: ", determinant_A)
print("Inverse of this matrix is:\n " , inverse_A)