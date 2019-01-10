n = int(input())
d={}
for i in range(n):
    inp = input()
    if(inp in d):
        d[inp]+=1
    else:
        d[inp]=1
print(len(d))
print(*d.values())
