# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to interpolate a set of data points (add new data points
# based on previous data) using the SciPy library.

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interpolate

x = np.arange(5, 20)
# Gets exponential value of x
# and divides each element by 3
y = np.exp(x / 3.0)
# Interpolates a function in one dimension
f = interpolate.interp1d(x, y)
x1 = np.arange(6, 12)
# Use interpolation function returned by "interpld"
y1 = f(x1)
# Plots x1 and y1 between x and y
plt.plot(x, y, 'o', x1, y1, '--')
plt.show()

print(np.exp(20/3))
