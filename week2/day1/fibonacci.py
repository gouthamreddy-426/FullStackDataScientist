def fib(n):
    res = [0,1]
    a = 0
    b = 1
    for i in range(n-2):
        c = a+b
        res.append(c)
        a,b = b,c
    return res

n = int(input("Enter n "))
print(fib(n))