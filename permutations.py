from itertools import permutations
s,n = raw_input().split()
print([''.join(i) for i in permutations(sorted(s),int(n))],sep=='\n')
