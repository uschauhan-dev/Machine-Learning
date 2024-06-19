import pandas as pd

data1 = pd.read_csv("person_details.csv")
#question1
print(data1.iloc[0:3,0:2])
print()
#question2
print(data1.loc[data1['Living Expenses']>3500])
print()
#question4
print(data1.iloc[2:8, :])
#question3
print()
print(data1.loc[data1["Gender"]=="Female"]) & (data1["City"].isin(["New York", "Los Angeles"])["Name","Age"])