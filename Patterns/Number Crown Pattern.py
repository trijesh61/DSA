#Number Crown Pattern
n=int(input())
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end='')
    print(" "*((2*(n-1))-2*i),end='')
    for j in range(i,0,-1):
        print(j,end='')
    print()