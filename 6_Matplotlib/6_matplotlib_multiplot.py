# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to add multiple plots to a single graph
# using the matplotlib function.


import numpy as np
import matplotlib.pyplot as plt


# Function used for plotting a
# function
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


# Two functions over a specific range
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

# Subplot is used to handle multiple plots
# 2 plots, 1 horizontal plot, this is the 1st lot
plt.subplot(211)
# Plots t1 and t2 by plugging into f(t) function
plt.plot(t1, f(t1), "bo", t2, f(t2))

# 2 plots, 1 horizontal plot, this is the 2nd plot
plt.subplot(212)
# Plots t1 and t2 by plugging into f(t) function
plt.plot(t2, np.cos(2 * np.pi * t2))
plt.show()
