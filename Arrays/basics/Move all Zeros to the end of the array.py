#Move all Zeros to the end of the array

a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i]==0:
        a.pop(i)
        a.append(0)
print(a)