import numpy as np
from numpy import random

#19. შეავსეთ 10x10 მატრიცა შემთხვევითი რიცხვებით [0, 10] შუალედიდან. წაშალეთ
#კლავიატურიდან შეტანილი რიცხვი. გამოიყენეთ numpy ბიბლიოთეკა.

nmin, nmax = 1, 10
matr = np.random.randint(nmin, nmax, size=(1, 10, 10))
print(matr)