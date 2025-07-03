# Problem:  Given an array of size n, sort the array using Merge Sort.

def merge_sort(arr):
    if len(arr)<=1:
        return
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_lists(left,right,arr)

def merge_two_sorted_lists(left,right,arr):
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            