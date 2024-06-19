#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:47:30 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:21:10 2024

@author: Student
"""
import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv("ComputerSales.csv")

print(df.info())
plt.subplot(1,2,1)
plt.hist(df['Sale Price']) #by default the bin value is set to 10

plt.subplot(1,2,2)
plt.hist(df['Profit'])
plt.xlabel("Price")
plt.ylabel("Count")
plt.grid()
plt.tight_layout()