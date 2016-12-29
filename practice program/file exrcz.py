fname=input("Enter a file name :")
if len==0:
    fname='mbox-short.txt'
fhand=open(fname)
for line in fhand:
    line=line.strip().upper()
print(line)
