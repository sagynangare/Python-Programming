counts=dict()
names=['csev','cwen','csav','zquin','cwen']
for name in names:
    if name not in names:
        counts[name]=1
    else:
        counts[name]=counts.get(name,0)+1
print(counts)
