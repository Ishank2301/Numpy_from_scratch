import numpy as np
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])
teenagers = ages[ages<18]
adults = ages[(ages>=18) & (ages<=65)]
print(ages > 65)