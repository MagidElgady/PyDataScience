# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to create a basic numpy array
# and how they are used

# np is a common shorthand
# used for numpy
import numpy as np

# Numpy can be used to create an
# array like a matrix
a = np.array([1, 2, 3])

print("This is a 1D numpy array:", a)

# We can add multiple dimensions to this array
# by separating each group with a comma (,)
b = np.array([(1, 2, 3), (4, 5, 6)])

print("This is a 2D numpy array:", b)
