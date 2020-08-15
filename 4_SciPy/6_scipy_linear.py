# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson shows how to solve linear algebraic equations using the SciPy
# library as well as how fast SciPy can be.

import numpy as np
# Linalg allows us to perform linear
# algebraic functions
from scipy import linalg

a = np.array([[1, 2], [3, 4]])
# Computes the inverse of the a matrix
# using the inv function
b = linalg.inv(a)
print(b)
