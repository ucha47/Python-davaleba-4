import numpy as np
from numpy import random

arr1 = random.randint(10, size=4)
arr2 = random.randint(10, size=4)
arr3 = np.multiply(arr1, arr2)
print(arr3)