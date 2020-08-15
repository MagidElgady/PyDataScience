# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how seaborn makes it easy to improve the aesthetics
# of a graph.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set method allows you to change
# the appearance of a graph using
# available themes
sns.set(style="darkgrid")
a = sns.load_dataset("flights")
b = sns.PairGrid(a)
b.map(plt.scatter)

plt.show()


sns.set(style="white", color_codes=True)
a = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=a)
# Removes top and right spines from plots and
# shifts the x-axis by 10 pixels
sns.despine(offset=10, trim=True)

plt.show()

# Available colour palettes you can choose from
c = sns.color_palette()
sns.palplot(c)
# Shows the different colours available to you
plt.show()
