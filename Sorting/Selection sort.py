#Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    min=i
    for j in range(i+1,n):
        if a[min]>a[j]:
            min=j
    a[i],a[min]=a[min],a[i]
print(a)
