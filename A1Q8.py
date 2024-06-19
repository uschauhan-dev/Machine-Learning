num = int(input("Enter a number to check its divisibilty with 9:"))

n = num
sum=0.0

while num!=0:
    r=num%10
    sum=sum+r
    num=num//10

if(sum % 9==0):
    print("Number",n," is divisible by 9")
else:
    print("Number",n," is not divisible by 9")    

