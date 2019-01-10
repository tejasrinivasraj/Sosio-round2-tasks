import itertools
s=input()
for i,g in itertools.groupby(s):
    print("(%r, %r)"%(len(list(g)),int(i[0])),end=" ")
