# PANDAS

# Pandas is a Python module that helps us read and manipulate data. What's cool about pandas is that you can take in data and view it as a table that's human readable, but it can also be interpreted numerically so that you can do lots of computations with it. We call the table of data a DataFrame.

# We need to start by importing Pandas. It's standard practice to nickname it pd so that it's faster to type later on.

import pandas as pd 

# We're going to pull the data into pandas so we can view it as a DataFrame.
# The read_csv function takes a file in csv format and converts it to a Pandas DataFrame.

df = pd.read_csv('https://sololearn.com//uploads/files/titanic.csv') # The object df is now our pandas dataframe with the Titanic dataset.

# Now we can use the head method to look at the data.
# The head method returns the first 5 rows of the DataFrame.
print(df.head())

# In pandas, we can use the describe method. It returns a table of statistics about the columns.
print(df.describe())


# SELECTING A SINGLE COLOUMN
#  To select a single column, we use the square brackets and the column name. To select a single column, we use the square brackets and the column name.

col = df["Fare"]
print(col)

# SELECTING MULTIPLE COLOUMNS
# When selecting a single column from a Pandas DataFrame, we use single square brackets. When selecting multiple columns, we use double square brackets.

small_df = df[['Age','Sex','Survived']]
print(small_df.head()) # Here we use head method to print only 5 rows


# We can easily create a new column in our DataFrame that is True if the passenger is male and False if they’re female.
df['male'] = df['Sex'] == 'male'
print(df.head())

df['First Class'] = df['Pclass'] == 1
print(df.head())


# Converting from a Pandas Series to a Numpy Array

# we use the values attribute to get the values as a numpy array.
# The values attribute of a Pandas Series give the data as a numpy array.
print(df['Fare'].values)


# Converting from a Pandas DataFrame to a Numpy Array.
# The values attribute of a Pandas DataFrame give the data as a 2d numpy array.
print(df[['Age','Sex','Survived']].values)



# Numpy Shape Attribute

arr = df[['Age','Pclass','Fare']].values
print(arr.shape)
# output
# (887, 3) it means 887 rows and 3 coloumns


# Select from a Numpy Array..
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr[0,1]) # It means his will be the 2nd column of the 1st row (remember that we start counting at 0).
print(arr[0]) # We can also select a single row, for example, the whole row of the first passenger
print(arr[:,2]) # We can also select a single row, for example, the whole row of the first passenger:


# Masking...
# A mask is a boolean array (True/False values) that tells us which values from the array we’re interested in.

arr = df[['Pclass', 'Fare', 'Age']].values[:10] 
mask = arr[:,2]<18
print(arr[mask])
print(arr[arr[:,2]< 18])


# SUMMING AND COUNTING

arr = df[['Pclass', 'Fare', 'Age']].values 
mask = arr[:,2]<18
print(mask.sum()) # it counts only true values in array
print((arr[:,2]< 19).sum()) # It counts all the values in array

