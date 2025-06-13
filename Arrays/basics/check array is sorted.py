#Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def check(a):
    l,t=len(a),True
    for i in range(l-1):
        if a[i]>a[i+1]:
            t=False
    return t
a=list(map(int,input().split()))
if check(a):
    print("Array is Sorted!")
else:
    print("Array is not sorted!")