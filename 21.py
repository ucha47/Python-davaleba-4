import numpy as np
from numpy import random

#21. შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. შეცვალეთ ყველა
#0-ის მნიშვნელობა 1-ით. გამოიყენეთ numpy ბიბლიოთეკა.

nmin, nmax = 0, 10
matr = np.random.randint(nmin, nmax, size=(1, 10, 10))
matr[matr < 1] = 1
print(matr)