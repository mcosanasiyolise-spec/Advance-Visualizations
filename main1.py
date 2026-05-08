import seaborn as sns
import numpy as np
sns.set_theme(); np.random.seed(0)
x = np.random.randn(100)
ax = sns.displot(x)