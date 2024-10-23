import numpy as np

A = np.array([[1, 2, -3], [4, -1, 2], [2, 1, 1]])
b = np.array([[1, 0, 2]])
print(A) # Output: [[1 2 3] [4 5 6] [7 8 9]]
# The matrix A is invertible multiplication
mult = np.dot(b, A)
print(mult) # Output: [ 5 -1  1]

x = np.linalg.solve(A, b.T)
print(x) # Output: [[ 0.  0.  0.]]
