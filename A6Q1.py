#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:41:27 2024

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
#1
df = pd.read_csv("/Users/Uday/Spyder-Programs/Iris.csv")
#2
print(df.head(5))
print(df.columns)
df.columns = ['id','sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
print(df.head(5))
#3
print(df.describe())
#4
sns.boxplot(data=df, x='class', y='sepal-length')
plt.savefig('plot1.png')
plt.close()
#5
sns.boxplot(data=df, x='class', y='sepal-width')
plt.savefig('plot2.png')
plt.close()
#6
df['class'].value_counts().plot.bar()
plt.savefig('plot3.png')
plt.close()