# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:32:43 2024

@author: Student
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# 1. Exploring the data, cleaning if required, and printing the head of the data.
url = "https://github.com/gauraviiita/Supervised_ML/raw/main/Datasets/MLR_datasets/Student_Performance.csv"
df = pd.read_csv(url)

print("Head of the DataFrame:")
print(df.head())

# 2. Apply the preprocessing techniques for object columns.
# Assuming there are object columns that need to be preprocessed
object_columns = df.select_dtypes(include=['object']).columns
if not object_columns.empty:
    label_encoder = LabelEncoder()
    for col in object_columns:
        df[col] = label_encoder.fit_transform(df[col])

# 3. Create plots to understand more about the distribution.
plt.figure(figsize=(12, 8))
for i, col in enumerate(df.columns):
    plt.subplot(3, 3, i+1)
    df[col].hist()
    plt.title(col)
plt.tight_layout()
plt.show()

# 4. Separate the dependent and the independent variables and store them in newly defined variables.
X = df.drop(columns=['Performance Index'])  # independent variables
y = df['Performance Index']                 # dependent variable

# 5. Split the data into 30% test and 70% train.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 6. Train the linear regression model and predict the values for test set data.
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 7. Evaluate the built model using root mean squared error and R2 score.
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nEvaluation metrics:")
print("Root Mean Squared Error:", rmse)
print("R2 Score:", r2)