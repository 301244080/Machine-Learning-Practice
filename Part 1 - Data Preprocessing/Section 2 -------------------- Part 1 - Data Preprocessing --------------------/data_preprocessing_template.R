# Data Preprocessing

#Importing the dataset
dataset = read.csv('Data.csv')
# dataset = dataset[, 2:3]
# Taking care of missing data

# taking column age
# 1. if value of column age is missing
# 2. replace the missing value with average
# 3. the value to return if the first condition is not met


# Encoding categorical data
# transform to column of factors
# Click F1 to view the function

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
# Country and Puchased are factor variables not numeric variables