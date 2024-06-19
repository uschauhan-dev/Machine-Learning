#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:42:48 2024

@author: Uday
"""


import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(-np.pi, np.pi, 200)
print(x_values)

sin_values = np.sin(x_values)
cos_values = np.cos(x_values)
tan_values = np.tan(x_values)

plt.figure(figsize=(8,6))

plt.subplot(1,3,1)
plt.plot(sin_values)

plt.subplot(1,3,2)
plt.plot(cos_values)

plt.subplot(1,3,3)
plt.plot(tan_values)

plt.tight_layout()
