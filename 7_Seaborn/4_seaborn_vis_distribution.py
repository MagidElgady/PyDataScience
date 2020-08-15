# Python Full Course - Learn Python in 12 Hours | Python Tutorial For Beginners | Edureka
# This lesson looks at how to visualise the distribution of a dataset
# with the context of it being univariate or bivariate.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Produces random data
c = np.random.normal(loc=5, size=100, scale=2)

# Produces a univariate distribution
sns.distplot(c)

# plt.show()


mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])

# Produces a bivariate distribution
sns.jointplot(x="x", y="y", data=df)

plt.show()
