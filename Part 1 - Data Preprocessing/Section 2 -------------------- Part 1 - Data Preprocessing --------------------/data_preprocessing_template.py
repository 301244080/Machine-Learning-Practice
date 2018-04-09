 #Data Preprocessing

 #Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# matrix of independent variables
# left: # of lines, in this case all lines
# Right # of columns, in this case all columns except for the last one
X = dataset.iloc[:, :-1].values

# Dependent variable vector
y = dataset.iloc[:, 3].values



#Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
# Do we need to fit and transform the dummy variables?
# It depends on the context
# Do we need to apply feature scaling on Y
# No, we don't need to. 