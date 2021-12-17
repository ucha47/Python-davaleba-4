import numpy as np
from numpy import random

arr1 = random.randint(10, size=3)
arr2 = random.randint(10, size=3)
arr3 = random.randint(10, size=3)
matr = np.matrix((arr1, arr2, arr3))
print(matr)

#18. შეავსეთ 3x3 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან.
# გამოიყენეთ numpy ბიბლიოთეკა.