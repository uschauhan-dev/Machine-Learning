num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
list=[]
for i in range(num1, num2+1):
    if i>1:
        for j in range(2, int((i/2)+1)):
            if i % j ==0:
                break
        else:
            list.append(i)
print(list)