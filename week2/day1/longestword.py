def longest(s):
    s = s.split()
    d = {}
    for i in s:
        d[len(i)] = i 
    a = max(d)
    return d[a]


s = input("Enter String ")
print(longest(s))