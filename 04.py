# SCIKIT-LEARN
# All of the basic machine learning algorithms are implemented in sklearn. We’ll see that with just a few lines of code we can build several different powerful models.

# import pandas as pd
# df = pd.read_csv('https://sololearn.com//uploads/files/titanic.csv')

# df['male'] = df['Sex'] == 'male'
# x = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
# # We target here a specific value
# y = df['Survived'].values
# print(x)
# print(y)

# Imort sklearn
from sklearn.linear_model import LogisticRegression
import pandas as pd
df = pd.read_csv('https://sololearn.com//uploads/files/titanic.csv')
x = df[['Fare','Age']].values
y = df["Survived"].values

# All sklearn models are built as Python classes. We first instantiate the class.

model = LogisticRegression()
# Fit method..
# The fit method is used for building the model. It takes two arguments: X (the features as a 2d numpy array) and y (the target as a 1d numpy array).
model.fit(x,y)

# Fitting the model means using the data to choose a line of best fit. We can see the coefficients with the coef_ and intercept_ attributes.

print(model.coef_, model.intercept_)

# [[ 0.01615949 -0.01549065]] [-0.51037152]
#These values mean that the equation is as follows:
# 0 = 0.0161594x + -0.01549065y + -0.51037152
