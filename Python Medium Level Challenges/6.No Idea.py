[n,m]=list(map(int, input().split()))
l = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happy = 0
for i in l:
    if(i in a):
        happy+=1
    elif(i in b):
        happy-=1
print(happy)
