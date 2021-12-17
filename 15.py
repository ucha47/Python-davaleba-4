import numpy as np
from numpy import random

list1 = np.array([1, 2, 3])
list2 = np.array([9, 3, 2])
list3 = np.array([8, 3, 5])
matr1 = np.matrix((list1, list2, list3))

list4 = list2
list5 = np.array([7, 7, 1])
list6 = np.array([5, 3, 0])
matr2 = np.matrix((list4, list5, list6))

matr3 = matr1 + matr2
#print(matr3)

l1 = random.randint(20, size=4)
l2 = random.randint(20, size=4)
l3 = random.randint(20, size=4)
l4 = random.randint(20, size=4)
l5 = random.randint(20, size=4)
l6 = random.randint(20, size=4)

m1 = np.matrix((l1, l2, l3))
m2 = np.matrix((l4, l5, l6))
m3 = m1 + m2

print(m3)