#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:46:20 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:56:55 2024

@author: Student
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

print(df.info())
print(df.shape)

print(df.head(2))

class_column = df.groupby("class").size()
print(class_column)

plt.pie(class_column)
