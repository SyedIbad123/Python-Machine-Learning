# Numpy is a python library that allows fast and easy mathematical operations to be performed on arrays.

# Here we import python library numpy as np fo array calculations
import numpy as np

data = [15,16,18,19,22,24,30,34]

print("Mean :" ,np.mean(data)) 
print("Median :" ,np.median(data)) 
# In percentile the first arguement is the varibale and second is the range of percentile..
print("50th percentile (median)", np.percentile(data, 50))
print("25th percentile :", np.percentile(data, 25))
print("75th percentile :", np.percentile(data, 75))

print("standard deviation :", np.std(data))
print("variance :", np.var(data))


