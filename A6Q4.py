#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:22:10 2024

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
df = pd.read_csv("/Users/Uday/Spyder-Programs/Iris.csv")
df.columns = ['id', 'sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
X = df.drop(columns=['class'])  
y = df['class']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
#1
model_svm_radial = svm.SVC(kernel='rbf')
#2
model_svm_radial.fit(x_train, y_train)
#3
y_predicted_radial= model_svm_radial.predict(x_test)
#4
report = classification_report(y_test,y_predicted_radial)
print(report)