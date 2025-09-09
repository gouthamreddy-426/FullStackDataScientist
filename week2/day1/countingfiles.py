import os
files = os.listdir(".")
pc,tc = 0,0
for i in files:
    if i.endswith(".py"):
        pc += 1
    elif i.endswith(".txt"):
        tc += 1
print("Text Files:",tc)
print("Python files:",pc)