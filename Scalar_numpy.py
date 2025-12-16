import numpy as np
array = np.array([1,2,3])
# scalar arithmetic
#We have already done this in our first file 
#Multiplication, Addition, Substraction, Divide, Power
#for power
a = array ** 2
print(a)

#Vectorized math function
#Actually also known as 1-D List/array

#How to round up of elements in list.
b = np.array([1.7,3,4.9,5.6])
print(np.round(b))

#How to round down of elements in list.
print(np.floor(b))

#How to round up.
print(np.ceil(b))

#Make a pie
print(np.pi)

#Exercised on vectorized math function and scalar arithmetic
 #Calculating the radius of circle.
radii = np.array([1,2,3])
print(np.pi *radii**2)

# Element wise arithmetic
arr1 = np.array([1,2,3])
arr2 = np.array([4,8,9])

print(arr1 + arr2)
print(arr1 ** arr2)
print(arr1 * arr2)
print(arr1 / arr2)
  


## Element Comparisons:
score = np.array([91,92,33,67,75,22])
print(score == 22)
print(score <= 60) # Score less than or Eqal to 60 
print(score <= 33)


# OR you can do this:
score[score< 60] = 0
print(score)







