##Broadcasting allows Numpy to perform operations on arrays(matrix)
#With different shapes by virtually expanding dimensions
# So they match the larger array's shape.{Just according to properties of Matrix arithmeticoperations}

#The dimensions have the same size.
#One of the dimensions have the size 1.{if arr1 = [m*n] and  arr2 = [n*p] then its neccesary for Numbeer of columns in a matrix must be equal to number of rows in another matrix.

#Let's take an example:

import numpy as np

a =np.array([1,2,3])
b =np.array([[1],[2],[3],[4]])

print(a.shape)
print(b.shape)

print(a * b)

#
ar =np.array([[1,2,3,6,7,8,9,10]])
br =np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(np.shape(ar))
print(np.shape(br))
print(ar*br)