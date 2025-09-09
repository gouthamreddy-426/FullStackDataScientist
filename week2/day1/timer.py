import time
n = int(input("Enter the countDown "))
while(n>0):
    print(n)
    time.sleep(1)
    n -= 1
print(0)
print("Time's Up")