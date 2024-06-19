#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:46:56 2024

@author: Uday
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:06:32 2024

@author: Student
"""

import seaborn as sns
import matplotlib.pyplot as plt

iris_data = sns.load_dataset("iris")

sns.pairplot(iris_data)