from collections import Counter 

s = input("Enter a string")
s = s.split()

d = Counter(s)
print(d)
