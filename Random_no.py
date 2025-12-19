import numpy as np
rng = np.random.default_rng() # seed used to present the same results
print(rng.integers(low=1,high=7, size= (3,2)))


#How to produce random float numbaers:
print(np.random.uniform(low=-1, high=1, size =3))

#How to shuffle an array:

array =  np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

# Random choice
arr = np.array(["apple=🍎", "banana=🍌", "Orange=🍊", "coconut=🥥", "PineApple=🍍"])
arr = rng.choice(arr, size =(3, 4))
print(arr)