# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:49:23 2024

@author: Student
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:43:35 2024

@author: Student
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder

# 1. Print the basic dataset information such as head, statistics and data info.
url = "https://github.com/gauraviiita/Supervised_ML/raw/main/Datasets/logistic_regression/Iris%20Dataset.csv"
df = pd.read_csv(url)

print("Head of the DataFrame:")
print(df.head())

print("\nStatistics of the DataFrame:")
print(df.describe())

print("\nInfo of the DataFrame:")
print(df.info())

# 2. Apply the preprocessing techniques to convert the target columns into numerical columns.
# Assuming the target column is 'Species'
label_encoder = LabelEncoder()
df['species'] = label_encoder.fit_transform(df['species'])

# 3. Create pair plots for input features.
sns.pairplot(df, hue='species')
plt.show()

# 4. Split the data into training and test data and fit our training data to a logistic regression model.
X = df.drop(columns=['species'])
y = df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Create a confusion matrix and accuracy score.
y_pred = model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

print("\nConfusion Matrix:")
print(conf_matrix)
print("\nAccuracy Score:", accuracy)