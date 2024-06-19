# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:23:02 2024

@author: Student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Downloading the dataset
df = pd.read_csv("https://github.com/gauraviiita/Supervised_ML/raw/main/Datasets/Chapter_2/swedish_insurance.csv")

# 1. Print the head of the data frame.
print("Head of the DataFrame:")
print(df.head())

# 2. Analyze the data by looking at the data types.
print("\nData types of columns:")
print(df.dtypes)

# 3. Create plots to understand more about the distribution.
plt.figure(figsize=(10, 6))
plt.scatter(df['X'], df['Y'])
plt.title('Scatter plot of X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# 4. Separate the dependent and the independent variables and store them in newly defined variables.
X = df[['X']]  # independent variable(s)
y = df['Y']    # dependent variable

# 5. Split the data into 25% test and 75% train.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)

# 6. Not necessary for linear regression as scikit-learn expects 2D arrays by default. 

# 7. Train the linear regression model and predict the values for test set data.
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 8. Evaluate the built model using root mean squared error and R2 score.
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation metrics:")
print("Root Mean Squared Error:", rmse)
print("R2 Score:", r2)