List=[1,7,0.9,55,34,-7]

max_element=List[0]

for i in range(0,len(List)):
    if max_element<List[i]:
        max_element=List[i]
print(max_element)