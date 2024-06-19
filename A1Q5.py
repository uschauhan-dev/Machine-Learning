#GCD of two numbers
def find_gcd(n1, n2):
    while n2:
        n1,n2=n2,n1%n2
    return n1
result=find_gcd(12,9)
print(result)