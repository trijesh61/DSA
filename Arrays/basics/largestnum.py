#Problem Statement: Given an array, we have to find the largest element in the array.

def findMax(ar):
    m=ar[0]
    for i in ar:
        if i>m:
            m=i
    return m


l=list(map(int,input().split()))
print("The largest Number in the List is :",findMax(l))