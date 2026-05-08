import seaborn as sns
import numpy as np
import pandas as pd

#Generate some random multivariate data
x, y = np.random.RandomState(8).multivatiate_normal([0, 0], [(1, 0), (0, 1)], 10000)
df = pd.DataFrame({"x": x, "y": y})