import sys
import os
import numpy as np
a = np.array([1,2,3,4,5,7])
print(a)

#Insertion element at the starting of array or list:
a = np.insert(a, 0, 4)
print(a)

# Appending in numpy:
np.append(a, 4)
print(a)

#Deleting an element
a = np.delete(a, 4)
print(a)


#Some arithmatical operation in list 
#Multiplication:
a = a * 2
print(a)
print(type(a))

#Addition:
a = a+3
print(a)
#Add a in a
a += a
print(a)

#Add 1 or any numeriical number in arr:
a += 1
print(a)

#Subtraction:
a = a-2
print(a)

#Divide:
#Quotient
a = a//2
print(a)
#Remainder:
a = a/2
print((a))
