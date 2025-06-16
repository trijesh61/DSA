#Count Maximum Consecutive One's in the array

n=list(map(int,input().split()))
c,m=0,0
for i in n:
    if i==1:
        c+=1
    else:
        c=0
    if m<c:
        m=c
print(m)
