# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson will add labels to our graph e.g. title of graph, x-axis, y-axis
# using the matplotlib library.

import matplotlib.pyplot as plt

x = [5, 8, 10]
y = [12, 16, 6]

# Plots dataset to canvas
plt.plot(x, y)

# Adds labels to different parts of graph
plt.title("Info")
plt.ylabel("Y-axis")
plt.xlabel("X-axis")

# Shows our graph
plt.show()
