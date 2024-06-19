#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:48:18 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:38:45 2024

@author: Student
"""

import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv("ComputerSales.csv")
print(df.info())
print(df.shape)
print(df.describe)

plt.scatter(df['Sale Price'], df['Profit'])