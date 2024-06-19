#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:56:02 2024

@author: Uday
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import svm

# Read the dataset
df = pd.read_csv("/Users/Uday/Spyder-Programs/Iris.csv")

df.columns = ['id', 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
#1
X = df.drop(columns=['class']) 
y = df['class']
#2
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#3
model_svm = svm.SVC(kernel='linear')
#4
model_svm.fit(x_train, y_train)
#5
y_predicted = model_svm.predict(x_test)
#6
print(classification_report(y_test, y_predicted))