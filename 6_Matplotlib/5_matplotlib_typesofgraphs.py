# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson will look at how to plot the different types of graphs
# using matplotlib.

import matplotlib.pyplot as plt

# Bar graphs: Used to represent discrete data

# We use the .bar method to plot a bar graph
# with the form ([x], [y], label of bar, colour of bar)
# plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="Example One")
# plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="Example Two", color="g")

# Label the axis'
# plt.xlabel("Bar Number")
# plt.ylabel("Bar Height")
# plt.title("Bar graph")

# plt.legend()
# plt.show()


# Histograms: Shows frequency of a specific data point e.g.
# how many times you see 42.

# # Data
# population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42, 4, 99, 99, 102, 110,
#                    120, 121, 122, 130, 111, 115, 112, 80, 75, 65, 54, 44, 43, 42, 48]

# # Separates data into bins to show many times you see a specific
# # point e.g.
# bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

# # .hist is used to show histograms with x,y axis
# plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)

# # Adds labels for each of the axis
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Histogram")

# plt.legend()
# plt.show()


# Scatter Plot: Used to show correlation between two variables

# Data sets
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [5, 2, 4, 2, 1, 4, 5, 2]

# # Use the .scatter method to plot a scatter graph with following
# # arguments: data, data, label and colour of points
# plt.scatter(x, y, label="skitscat", color="k")

# # Labels for graph
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Scatter Plot")

# # Only 1 colour so legend isn't shown
# plt.legend()
# # Plot the scatter graph
# plt.show()

# Stack/Area plot: Used to track the changes in two related groups
# that are a part of a category

# days = [1, 2, 3, 4, 5]

# sleeping = [7, 8, 6, 11, 7]
# eating = [2, 3, 4, 3, 2]
# working = [7, 8, 7, 2, 2]
# playing = [8, 5, 7, 8, 13]

# # Lines are empty i.e. have no names as they're not needed.
# # Instead they are labeled.
# plt.plot([], [], color="m", label="Sleeping", linewidth=5)
# plt.plot([], [], color="c", label="Eating", linewidth=5)
# plt.plot([], [], color="r", label="Working", linewidth=5)
# plt.plot([], [], color="k", label="Playing", linewidth=5)

# plt.stackplot(days, sleeping, eating, working,
#               playing, colors=["m", "c", "r", "k"])

# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Stack Plot")
# plt.legend()
# plt.show()

# Pie Charts: Used to break down a category
# into subcategories by percentage e.g. time spent or budget

# Sizes for each portion of the pie
slices = [7, 2, 2, 13]
activities = ["sleeping", "eating", "working", "playing"]
cols = ["c", "m", "r", "b"]

# Use .pie to plot a pie chart with the following arguments:
# data, labels, colours, starting angle i.e. 90 means we have a
# vertical line, shadow for each of the portions, explode pulls out
# a specific portion e.g. the eating section and autopct gives
# each portion to 0.1 dp.
plt.pie(slices, labels=activities, colors=cols, startangle=90,
        shadow=True, explode=(0, 0.1, 0, 0), autopct="%1.1f%%")

plt.title("Pie Chart")
plt.show()
