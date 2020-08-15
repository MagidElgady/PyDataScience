# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to plot multiple plots using the seaborn library.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = sns.load_dataset("iris")
# FacetGrid is used to plot multiple
# graphs at once
b = sns.FacetGrid(a, col="species")
# Plots the points as a histogram
# with each having the x-axis as "sepal_length"
b.map(plt.hist, "sepal_length")

plt.show()

a = sns.load_dataset("flights")
# Produces multiple graphs as pairs
# in a grid
b = sns.PairGrid(a)
# Produces a scatterplot
b.map(plt.scatter)

plt.show()
