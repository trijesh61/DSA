#number that appears once, and the other numbers twice

n=list(map(int,input().split()))
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    if j==1:
        print(i)