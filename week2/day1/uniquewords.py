def unique(s):
    s = s.split()
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d
s = input("Enter a string ")
print(unique(s))