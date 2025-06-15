#Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.

a=list(map(int,input().split()))
s=int(input("Enter Element to be searched:"))
index=-1
for i in range(len(a)):
    if a[i]==s:
        index=i
        break
print("The Element is present at the index :",i)
    