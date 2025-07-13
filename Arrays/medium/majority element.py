#Problem Statement: Given an array of N integers,
# write a program to return an element that occurs more than N/2 times in the given array.
# You may consider that such an element always exists in the array.
def find(n,arr):
    t=n/2
    c=0
    el=0
    for i in arr:
        if c==0:
            c=1
            el=i
        elif el==i:
            c+=1
        else:
            c-=1
    
    cnt1=arr.count(el)
    if cnt1>t:
        return el
    return -1



n=int(input())
arr=list(map(int,input().split()))
t=find(n,arr)
print(t)