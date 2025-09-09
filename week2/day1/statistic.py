import statistics
l = list(map(int,input("Enter Scores ").split()))
print("mean = ",statistics.mean(l))
print("Median =",statistics.median(l))
print("Varience =",statistics.variance(l))