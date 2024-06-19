# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:14:31 2024

@author: Student
"""
#plt.scatter(df['SML_scores'],df['AD_scores'])
#plt.xlabel("SML Scores")
#plt.ylabel("AD Scores")
#plt.title("Scatter plot")
#plt.grid(axis='y')


import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

#load dataset
digits_data = load_digits()
X = digits_data.data
y = digits_data.target

#load the model
pca_model = PCA(n_components=2)

New_X = pca_model.fit_transform(X)

plt.figure(figsize=(8,6))
plt.scatter(New_X[:, 0],New_X[:,1], c=y, cmap="Reds")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
plt.show()
