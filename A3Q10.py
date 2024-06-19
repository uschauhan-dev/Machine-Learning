#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:49:10 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:52:48 2024

@author: Student
"""

import pandas as pd

from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("Housing.csv")
print(df.head(2))
print(df.info())

df['mainroad'] = LabelEncoder().fit_transform(df['mainroad'])
df['guestroom'] = LabelEncoder().fit_transform(df['guestroom'])
df['basement'] = LabelEncoder().fit_transform(df['basement'])
df['hotwaterheating'] = LabelEncoder().fit_transform(df['hotwaterheating'])
df['airconditioning'] = LabelEncoder().fit_transform(df['airconditioning'])
df['prefarea'] = LabelEncoder().fit_transform(df['prefarea'])
df['furnishingstatus'] = LabelEncoder().fit_transform(df['furnishingstatus'])

print(df.info())

