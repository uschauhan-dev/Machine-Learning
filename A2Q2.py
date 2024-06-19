import pandas as pd

data1 = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack'],
'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male'],
'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio',
'San Diego', 'Dallas', 'San Jose'],
'Living Expenses': [3000, 3500, 3200, 2800, 4000, 3300, 3100, 3700, 2900, 3800]
}

data2= {'Name': ['Uday', 'Rohan'],
        'Gender': ['Male', 'Male'],
        'Age': [20, 20],
        'City': ['New York', 'Los Angeles'],
        'Living Expenses': [1500, 2500]
        }

df1= pd.DataFrame(data1)
df2=pd.DataFrame(data2)

df =pd.concat([df1, df2])

print(df)