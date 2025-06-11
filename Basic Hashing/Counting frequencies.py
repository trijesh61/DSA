#Problem statement: Given an array, we have found the number of occurrences of each element in the array.

arr=list(map(int,input().split()))
c={}
for i in range(len(arr)):
    if arr[i] not in c:
        c[arr[i]]=1
    else:
        c[arr[i]]+=1
for k,v in c.items():
    print(f"{k}:{v}")