#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:48:41 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:47:19 2024

@author: Student
"""

import pandas as pd

from sklearn.model_selection import train_test_split

df=pd.read_csv("Housing.csv")
print(df.head(2))
print(df.info())

Y= df.iloc[:,0]
X=df.iloc[:,1:]

train_x, train_y, test_x, test_y = train_test_split(X,Y, test_size=0.3)

print(train_x.shape)
print(train_y.shape)