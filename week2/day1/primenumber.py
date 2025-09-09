import math
def prime(n):

    def isPrime(m):
        for i in range(2,int(math.sqrt(m))+1):
            if m%i == 0:
                return False
        return True
    
    if n < 2:
        return "Prime numbers Starts with 2"
    l = []
    for i in range(2,n+1):
       if isPrime(i):
           l.append(i)
    return l

n = int(input("Enter n "))
print(prime(n))