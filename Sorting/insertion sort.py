#Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

 
n=int(input())
elements=list(map(int,input().split()))
for i in range(1,n):
    temp=elements[i]
    j=i-1
    while j>=0 and temp<elements[j]:
        elements[j+1]=elements[j]
        j=j-1
    elements[j+1]=temp
print(elements)