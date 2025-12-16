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
#or better see in 1d array
sc1 = np.array([1,5,7,9,3,4,5,5,6])

# How actually slicing work on array
# array[start:end:step]
# For slicing we use the same general method that is listed above,For slicing we selecting a starting  index and end index till we want to slice , we can also add steps so we can only slice every 2nd element at the index or to peform even odd or interval slicing.
print(sc1[1:]) #print every element except the first element.Slice the first elemnent.
print(sc1[-1:]) #slice every element except the last element.If we change -1 to{-2,-3,-4} same amount of element from last will be printed
print(sc1[-5:-1]) #will print last 5 elements but the last of the fifth will be sliced.
print(sc1[:-1]) # slice the last element only.
print(sc1[1:8:2]) #Print every second element of index 1 to 8 not including 8
print(sc1[1:-4]) #print element from index 2nd to index 6th{here -4 is the number of element sliced from the end of list}.
print(sc1[::-1]) #To print an list in opposite order(start=0:end=9:step=-1)){By increasing step (-2,-3) we will get an opposite array of that interval elements }

#Slicing in 3d array:
sc = np.array([[1,2,3,4], 
               [5,6,7,8], 
               [9,0,1,2], 
               [4,6,9,3]])

#General = arr[start:end:step{for row},start:end:step]{for column}]

print(sc[-1:])
print(sc[:-1])
result = sc[0:1] + sc[-1:]
print(result)
print(sc[0,0]) #if we want to print any particular element of the 2d array.
print(sc[:, -1]) # Column  operations through{start:end:step}= End for column operation.
print(sc[0:2,:-2]) #Selected 1st and 2nd row than did column operation by printing only the firdst 2 columns.
print(sc[::-1])
print(sc[1:-1,1:-1 ]) 
print(sc[2:,-2:][::-1])