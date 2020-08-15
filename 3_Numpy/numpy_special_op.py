# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at the special maths functions you
# can use with numpy such as sine, cosine, e, log and more.

import numpy as np
import matplotlib.pyplot as plt

# Creates x-axis between 0 and 3*pi
# with 0.1 increments
x = np.arange(0, 3 * np.pi, 0.1)

# Draws sine of x (can be cos or tan)
y = np.sin(x)

# Plots x and y
plt.plot(x, y)

# Shows plot to user
plt.show()

ar = np.array([1, 2, 3])
print("Gets e^1, e^2 and e^3:", np.exp(ar))

print("Gets ln1, ln2 and ln3:", np.log(ar))

print("Gets in base 10, log1, log2 and log3:", np.log10(ar))
