import numpy as np
from numpy import random

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)

arr4 = random.randint(10, size=3)
arr5 = random.randint(10, size=3)
arr6 = np.concatenate((arr4, arr5))
print(arr6)