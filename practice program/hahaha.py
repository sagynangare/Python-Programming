import urllib
fhand=urllib.urlopen('https://py4inf.com/code/romeo.txt')
for line in fhand:
    print(line.strip)
    
