import numpy as np
a = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['J', 'H', 'I']],
          [['K', 'L', 'M'], ['N', 'O', 'P'], ['Q', 'R', 'S']],
          [['T', 'U', 'V'], ['W', 'X', 'Y'], ['J', 'Z', '']]],
         )

print(a.ndim)

#Chain Indexing:
print(a[0][0][0]) #RINT A
print(a[0][2][0]) #PRINT J
print(a[0][2][1]) #PRINT H
print(a[1][0][0]) #PRINT D


#Multidimensional Indexing:
print(a[2, 2, 1]) #PRINT Z
print(a[1, 2, 0]) #PRINT Q
print(a[0, 2, 1]) #PRINT H


#concetenation in arrays
word = a[0,0,0] + a[0,2,2] +a[0,1,0] + a[1,2,2]
print(word)

#Slicing in array:
sc = np.array([[1,2,3,4], 
               [5,6,7,8], 
               [9,0,1,2], 
               [4,67,9,3]])

#or better see in 1d array
sc1 = np.array([1,5,7,9,3,4,5,5,6])

# How actually slicing work on array
# array[start:end:step]
# For slicing we use the same general method that is listed above,For slicing we selecting a starting  index and end index till we want to slice , we can also add steps so we can only slice every 2nd element at the index or to peform even odd or interval slicing.
print(sc1[1:]) #print every element except the first element.Slice the first elemnent.
print(sc1[-1:]) #slice every element except the last element.
print(sc1[:-1]) # slice the last element only.
print(sc1[1:8])
print(sc1[:2])