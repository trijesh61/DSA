n=int(input())
s=0
for i in range(1,n+1):
    if i%2==0:
        s=0
    else:
        s=1
    for j in range(i):
        print(s,end=' ')
        s=(s+1)%2
    print()