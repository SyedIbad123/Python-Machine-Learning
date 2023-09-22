import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('https://sololearn.com//uploads/files/titanic.csv')
df["male"] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values
model = LogisticRegression()
model.fit(X,y)

# The first passenger in the dataset is:
# [3, True, 22.0, 1, 0, 7.25]
model.predict(X)
# This means the passenger is in Pclass 3, are male, are 22 years old, have 1 sibling/spouse aboard, 0 parents/child aboard, and paid $7.25. Let’s see what the model predicts for this passenger. Note that even with one datapoint, the predict method takes a 2-dimensional numpy array and returns a 1-dimensional numpy array.

print(model.predict([[3, True, 22.0, 1, 0, 7.25]]))
# The predict method returns an array of 1’s and 0’s, where 1 means the model predicts the passenger survived and 0 means the model predicts the passenger didn’t survive.

# OUTPUT:
# [0] It means that the person did'nt survive

print(model.predict(X[:5])) 
# [0 1 1 1 0]
print(y[:5]) 
# [0 1 1 1 0]


# Calculate the percentage of accuracy

y_pred = model.predict(X)
y == y_pred
print(model.score(X,y)) # The score method is used to calculate the accuracy of our model

# This can be done by using different methods
print((y == y_pred).sum()/ y.shape[0])

# OUTPUT:
# 0.8049605411499436 It means the model is 80.5% accurate






