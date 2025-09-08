import random
import string
def generatePassword(n):
    ch = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(ch,k = n))
    return password
n = int(input("Enter length of a password "))
print(generatePassword(n))
