# MATPLOTLIB
# We can use the matplotlib library to plot our data. Plotting the data can often help us build intuition about our data.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://sololearn.com//uploads/files/titanic.csv')

# We use the scatter function to plot our data. The first argument of the scatter function is the x-axis (horizontal direction) and the second argument is the y-axis (vertical direction).
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])
plt.xlabel('Age')
plt.ylabel('Fare')
 


# LINE

# The plot function does just that. The following draws a line to approximately separate the 1st class from the 2nd and 3rd class. From eyeballing, we’ll put the line from (0, 85) to (80, 5). Our syntax below has a list of the x values and a list of the y values.

plt.plot([0, 80], [85, 5])
plt.show() 