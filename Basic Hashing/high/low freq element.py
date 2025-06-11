arr=list(map(int,input().split()))
c={}
for i in range(len(arr)):
    if arr[i] not in c:
        c[arr[i]]=1
    else:
        c[arr[i]]+=1
min=min(c.values())
max=max(c.values())
for i in c.keys():
    if c[i]==min:
        mi=i
    if c[i]==max:
        ma=i
print("maximum:",ma)
print("minimum:",mi)