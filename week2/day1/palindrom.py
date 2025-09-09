def palindrome(s):
    s = s.lower()
    s = s.replace(" ","")
    return s == s[::-1]



s = input("Enter String ")
print(palindrome(s))
