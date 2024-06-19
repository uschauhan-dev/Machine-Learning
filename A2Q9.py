import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

students_info ={"Students":['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
               "SML_scores" : [85, 90, 70, 80, 75],
               "AD_scores" :[80, 75, 85, 70, 90] } 


df= pd.DataFrame(students_info)
print(df.shape)
print(df.head())

plt.figure(figsize=(8,6))

plt.subplot(2,2,1)
plt.bar(df['Students'], df['SML_scores'])
plt.xlabel("Students name")
plt.ylabel("SML scores")
plt.title("SML Scores for each student")
plt.grid()

plt.subplot(2,2,2)
plt.hist(df['AD_scores'], bins=3)
plt.xlabel("Students info")
plt.ylabel("AD marks")
plt.title("AD scores for each student")
plt.grid(axis='x')

plt.subplot(2,2,3)
plt.scatter(df['SML_scores'],df['AD_scores'])
plt.xlabel("SML Scores")
plt.ylabel("AD Scores")
plt.title("Scatter plot")
plt.grid(axis='y')

plt.subplot(2,2,4)
plt.pie(df['SML_scores'], labels = df['Students'])
plt.title("Pie plot")

plt.tight_layout()
plt.suptitle("Question no. 9")
plt.savefig("Q9.jpg")


