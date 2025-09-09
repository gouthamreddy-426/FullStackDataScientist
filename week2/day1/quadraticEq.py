import math
a,b,c = map(int,input("Enter a b c values ").split())
d = b**2 - 4*a*c 
if d > 0:
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    print("Quadratic equation has 2 roots",r1,r2)
elif d == 0:
    print("Equation has only 1 root :",(-b/(2*a)))
else:
    r = -b/(2*a)
    i = math.sqrt(-d)/(2*a)
    print(f"Quadratic equation has imaginary roots {r} + {i}i  ,  {r}-{i}i")