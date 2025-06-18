#Move all Zeros to the end of the array

a=list(map(int,input().split()))
pos=0
for i in range(len(a)):
    if a[i]!=0:
        a[i],a[pos]=a[pos],a[i]
        pos+=1
    