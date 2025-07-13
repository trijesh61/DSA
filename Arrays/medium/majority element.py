#Problem Statement: Given an array of N integers,
# write a program to return an element that occurs more than N/2 times in the given array.
# You may consider that such an element always exists in the array.
def find(n,arr):
    t=n//2
    for i in arr:
        if arr.count(i)>=t:
            return i

n=int(input())
arr=list(map(int,input().split()))
t=find(n,arr)
print(t)