import math
n = int(input("Enter a number "))
while(True):
    print("==Calculator==")
    print("1.sqrt\n2.factorial\n3.sin\n4.cos\n5.exit")
    ch = int(input("Enter your choice "))
    if ch == 1:
        print(math.sqrt(n))
    elif ch == 2:
        print(math.factorial(n))
    elif ch == 3:
        print(math.sin(math.radians(n)))
    elif ch == 4:
        print(math.cos(math.radians(n)))
    elif ch == 5:
        break
    else:
        print("Invalid")
    
