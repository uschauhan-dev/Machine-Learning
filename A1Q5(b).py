num1=int(input('Enter the number 1:'))
num2=int(input('Enter the number 2:'))

while(num1%num2!=0):
    r=num1%num2
    num1=num2
    num2=r
print(num2)