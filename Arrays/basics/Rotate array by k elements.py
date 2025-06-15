#Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

a=list(map(int,input().split()))
n=len(a)
k=int(input("Enter no of positions:"))
pos=input("Enter the sirection to shift:")
if pos.lower()=='right':
    for j in range(k):
        m=a[-1]
        for i in range(n-1,0,-1):
            
            a[i]=a[i-1]
        a[0]=m
elif pos.lower()=='left':
    for j in range(k):
        m=a[0]
        for i in range(1,n):
            a[i-1]=a[i]
        a[-1]=m
print(a)