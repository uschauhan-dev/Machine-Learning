num=int(input("Enter anumber between 0 and 1000: "))

n = num
sum=0

while num!=0:
    r=num%10
    sum=sum+r
    num=num//10

print("Sum of the digits of the number is:", sum)