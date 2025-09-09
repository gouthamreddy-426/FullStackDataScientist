def calgrade(marks):
    a = sum(marks)//len(marks)
    if a >= 90:
        g = "A"
    elif 80 <= a <= 89:
        g = "B"
    elif 70 <= a <= 79:
        g = "C"
    elif 60 <= a <= 69:
        g = "D"
    else:
        g = "F"
    return g
marks = list(map(int,input("Enter the marks").split()))
print("Grade:",calgrade(marks))
