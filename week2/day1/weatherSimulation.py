import random
temp = random.randint(-10,40)
if temp < 0:
    w = "Snowy"
elif 0<=temp<=10:
    w = "Cold"
elif 11<=temp<=20:
    w = "Pleasant"
elif 21<=temp<=30:
    w = "warm"
elif 31<=temp<=40:
    w = "Sunny"
else:
    w = "Very Hot"
print("weather:",w,",temp:",temp)