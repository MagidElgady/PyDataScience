# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson will look at how to divide a main variable into discrete groups
# i.e. categories.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Catplot: Category plot used to divide a main variable into subcategories

# Load tips dataset from GitHub repository
a = sns.load_dataset("tips")

# Produces scatter plot of the tips data
sns.catplot(x="day", y="total_bill", data=a)

plt.show()
