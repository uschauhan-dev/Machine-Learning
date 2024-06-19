# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:39:16 2024

@author: Student
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# Load the dataset
data = pd.read_csv("diabetes.csv")

# Task 1: Print basic dataset information
print("Head:")
print(data.head())
print("\nStatistics:")
print(data.describe())
print("\nData info:")
print(data.info())

# Task 2: Box plots for different attributes with respect to Outcome
plt.figure(figsize=(12, 8))
for i, col in enumerate(data.columns[:-1]):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(x='Outcome', y=col, data=data)
plt.tight_layout()
plt.savefig("Q3Plot.png")

# Task 3: Pair plots of selected columns
selected_columns = ['Glucose', 'Age', 'DiabetesPedigreeFunction', 'BMI', 'Insulin', 'SkinThickness', 'BloodPressure', 'Outcome']
sns.pairplot(data[selected_columns], hue='Outcome')
plt.show()

# Task 4: Split the data into training and test sets
X = data.drop('Outcome', axis=1)
y = data['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Task 5: Fit logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Task 6: Create confusion matrix
y_pred = model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)
