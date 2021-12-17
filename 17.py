import numpy as np
from numpy import random

arr1 = random.randint(10, size=3)
arr2 = random.randint(10, size=3)
arr3 = random.randint(10, size=3)
matr1 = np.matrix((arr1, arr2, arr3))

arr4 = random.randint(10, size=3)
arr5 = random.randint(10, size=3)
arr6 = random.randint(10, size=3)
matr2 = np.matrix((arr4, arr5, arr6))

matr3 = np.multiply(matr1, matr2)
print(matr3)