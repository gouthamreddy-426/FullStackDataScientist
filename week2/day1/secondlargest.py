def secondlargest(l):
    if len(l) < 2:
        print("Cannot have second largest")
    else:
        fm,sm = float("-inf"),float("-inf")
        for i in l:
            if fm < i:
                sm = fm
                fm = i
            elif sm < i and fm > i:
                sm = i 
        if sm == float("-inf"):
            print("No second largest element present")
        else:
            print(sm)


l = list(map(int,input("Enter ").split()))
secondlargest(l)