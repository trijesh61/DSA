#Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

n=int(input())
a=list(map(int,input().split()))
for i in range(n-1):
    swapped=False
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j+1],a[j]=a[j],a[j+1]
            swapped=True
    if not swapped:
        break
print(a)