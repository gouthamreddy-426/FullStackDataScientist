def count(s):
    v,c = 0,0
    for i in s:
        if i.lower() in "aeiou":
            v += 1
        else:
            c += 1
    return v,c

s = input("Enter String ")    
v,c = count(s)
print("Vowels =",v,",Consonents =",c)