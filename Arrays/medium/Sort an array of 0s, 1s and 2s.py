#Problem Statement: Given an array consisting of only 0s, 1s, and 2s.
#Write a program to in-place sort the array without using inbuilt sort functions.
#( Expected: Single pass-O(N) and constant space)

def sort_array(arr):
    n=len(arr)
    low,mid,high=0,0,n-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1


n=list(map(int,input().split()))
sort_array(n)
print(n)