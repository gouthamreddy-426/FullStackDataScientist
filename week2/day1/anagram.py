def anagram(s1,s2):
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    return s1==s2

s1 = input("Enter String 1 ")
s2 = input("Enter String 2 ")
print(anagram(s1,s2))