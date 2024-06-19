import pandas as pd

data1 = pd.read_csv('person_details.csv')

#print(data1.head(2))

data2 = {'Name': ['Seeta', 'Geeta'],
         'Gender':['Female','Female'],
         "Age":[21,23],
         "City":['Prayagraj', 'Varanasi'],
         "Living Expenses": [2300, 7890]}

data2= pd.DataFrame(data2)

data3 = pd.concat([data1, data2],ignore_index=True)
print(data3.tail())