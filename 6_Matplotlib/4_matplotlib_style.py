# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson will look at adding colour, a legend and changing the width
# of the lines using the matplotlib library.

import matplotlib.pyplot as plt
from matplotlib import style

# Sets specific style for graph
style.use("ggplot")

x = [5, 8, 10]
y = [12, 16, 6]

x2 = [6, 9, 11]
y2 = [6, 15, 7]

# Sets line of x,y as green with a set width of 5 and
# a name of line one
plt.plot(x, y, 'g', label="line one", linewidth=5)
# Sets line of x2,y2 as green with a set width of 5 and
# a name of line two
plt.plot(x2, y2, 'c', label="line two", linewidth=5)

# Sets the labels of the graph
plt.title("Epic Info")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# Shows which colour is for which dataset
# e.g. x,y or x2, y2
plt.legend()
# Adds a grid with colour k or black
plt.grid(True, color="k")

# Shows the graph
plt.show()
