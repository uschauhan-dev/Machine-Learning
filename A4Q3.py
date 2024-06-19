# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:40:16 2024

@author: Student
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout

model = Sequential()

model.add(Input(shape=(1000,)))
model.add(Dense(units=512, activation ='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.15))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

print(model.summary())