import numpy as np
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])
print(np.sum(array)) #Sum of all the element of the array.
print(np.mean(array)) #Mean of the data.
print(np.std(array)) #Standard deviation of the data{Measure of sperad within your data}.
print(np.var(array)) #Variance = (Standard Deviation)^2{sqr of standard deviation}.
print(np.min(array)) # to get miunimum value.
print(np.max(array)) #To get maximum value.
print(np.argmin(array)) #To get position{index} minimum value.
print(np.argmax(array)) #To get position{index} maximum value.



# Row and column wise operations
print(np.sum(array, axis=0)) #Sum of all columns.
print(np.sum(array, axis=1)) #Sum of all rows.
