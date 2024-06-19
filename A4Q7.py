# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:25:53 2024

@author: Student
"""
#Step 1: Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import Ridge

#Step 2: Read the dataset
data = pd.read_csv("Housing Price data set.csv")
print(data.head())
print(data.info())

df = data.iloc[:, 1:]
print(df.info())
print(df.describe())

#Step 3: Visualize the dataset
plt.scatter(df["lotsize"], df["price"])

#Step 4: preprocessing
df["driveway"] = LabelEncoder().fit_transform(df["driveway"])
df["recroom"] = LabelEncoder().fit_transform(df["recroom"])
df["fullbase"] = LabelEncoder().fit_transform(df["fullbase"])
df["gashw"] = LabelEncoder().fit_transform(df["gashw"])
df["airco"] = LabelEncoder().fit_transform(df["airco"])
df["prefarea"] = LabelEncoder().fit_transform(df["prefarea"])

print(df.info())

X = df.iloc[:, 1: ]
y = df.iloc[:, 0]

#Step 5: Split data into train test
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.5, random_state = 2)

#Step 6: Build Linear Regression model
model = LinearRegression()

#Step 7: Train the model
model.fit(train_x, train_y)

#Step 8: predict the values for x_test
y_pred = model.predict(test_x)

plt.scatter(test_y, y_pred)
plt.xlabel("Actual data")
plt.ylabel("Predicted data")

#Step 9: Calculate the rmse, r2 score
mse_value = mean_squared_error(test_y, y_pred)

rmse_value = np.sqrt(mse_value)

print(f"Root mean squared value is: ", rmse_value)
print(f"R2 score value is : {r2_score(test_y, y_pred)}")



#(i) we are taking all the columns/features thats why maybe the accuracy is low
#so we need to drop the redundant columns to get high accuracy

#(ii) also we need the make the columns in the same range


