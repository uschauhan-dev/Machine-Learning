# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:42:10 2024

@author: Student
"""

import pandas as pd
from sklearn.preprocessing import Binarizer, LabelEncoder, LabelBinarizer

# Given dataset
data = {
    "City": ["New York", "Los Angeles", "Chicago", "Miami", "Boston"],
    "Temperature (C)": [20, 25, 15, 30, 18],
    "Humidity (%)": [65, 70, 60, 75, 55],
    "Month": ["January", "February", "March", "April", "May"],
    "Target": ["Yes", "No", "Yes", "No", "Yes"]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)
print(df.head())
print(df.info())


bins = Binarizer(threshold=20) #we use this to get smaller values; ie, range should match city range
bins1 = Binarizer(threshold = 65)
df["Temperature (C)"]=bins.fit_transform(df[["Temperature (C)"]])
print(df)

df["Humidity (%)"] = bins1.fit_transform(df[["Humidity (%)"]])
print(df)

#Label Encoder

df["City"] = LabelEncoder().fit_transform(df["City"])
df["Month"] = LabelEncoder().fit_transform(df["Month"])


print(df)

#Label Binarizer

df["Target"] = LabelBinarizer().fit_transform(df["Target"])
print(df)

df.to_csv("clean_data.csv", index=False)
