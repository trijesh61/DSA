# Problem Statement: Given an array of N integers, left rotate the array by one place.

l=list(map(int,input().split()))
n=len(l)
m=l[0]
for i in range(n-1):
    l[i]=l[i+1]
l[n-1]=m
print(l)