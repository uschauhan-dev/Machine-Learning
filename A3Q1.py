#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:40:35 2024

@author: Uday
"""

import pandas as pd
df = pd.read_csv("data.csv")
print(df)
print(df.shape)
print(df.isna().sum())