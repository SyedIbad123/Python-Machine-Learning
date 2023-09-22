# LOGISTIC REGRESSION WITH BREAST CANCER DATASET...

# Now that we’ve built up the tools to build a Logistic Regression model for a classification dataset.
# In the breast cancer dataset, each datapoint has measurements from an image of a breast mass and whether or not it’s cancerous. The goal will be to use these measurements to predict if the mass is cancerous.
# This dataset is built right into scikit-learn so we won’t need to read in a csv.

import pandas as pd
from sklearn.datasets import load_breast_cancer
cancer_data = load_breast_cancer()
print(cancer_data.keys()) # Keys method returns keys in the datasets
print(cancer_data['data']) # It prints the data
print(cancer_data['data'].shape) # shape method prints no of rows and columns
df = pd.DataFrame(cancer_data['data'], columns = cancer_data['feature_names'])
print(df.head())

print(cancer_data['target'].shape)
df['target'] = cancer_data['target']
print(df.head())



