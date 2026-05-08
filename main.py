# importing he required library
import seaborn as sns
import matplotlib.pyplot as plt

# read a titanic.csv file
df = sns.load_dataset('titanic')

# who v/s fare barplot
sns.barplot(x = 'who',
y = 'fare',
data = df)

# show the plot
plt.show()