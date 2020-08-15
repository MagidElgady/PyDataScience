# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson will look at data visualization and how to statistical relationships
# i.e. plotting a graph of data.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loads dataset from GitHub
a = sns.load_dataset("flights")
# Sets the axis, data and year for graph
# Hue changes the colour of the points depending
# on data e.g. the year is represented by different colours
sns.relplot(x="passengers", y="month", hue="year", data=a)

# Shows the above graph
# plt.show()

b = sns.load_dataset("tips")
# Produces a line graph
sns.relplot(x="time", y="tip", data=b, kind="line")

# Shows the above graph
plt.show()
