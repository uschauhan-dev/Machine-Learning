n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

def find_max_value(n1,n2,n3):
    def max_of_two(x,y):
        if x>y:
            return x
        else:
            return y
    a=max_of_two(n1,n2) 
    b=max_of_two(a,n3) 
    return b
result=find_max_value(n1,n2,n3)  
print (result)