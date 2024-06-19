# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:58:07 2024

@author: Student
"""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

diabetes_data = load_diabetes()
X = diabetes_data.data
y = diabetes_data.target

train_x, test_x, train_y, test_y = train_test_split(X, y, test_size=0.2)
print(train_x.shape)
print(test_x.shape)

model = LinearRegression()
model.fit(train_x, train_y)

print("weight coeffficient")
print(model.coef_)
print("Bias")
print(model.intercept_)


