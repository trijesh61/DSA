#Kadane's Algorithm : Maximum Subarray Sum in an Array

#Problem Statement: Given an integer array arr, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and returns its sum and prints the subarray.

def max_subarray_sum(arr):
    max_sum=arr[0]
    current_sum=arr[0]
    for i in range(1,len(arr)):
        current_sum=max(arr[i],current_sum+arr[i])
        max_sum=max(current_sum,max_sum)
    return max_sum

arr=list(map(int,input().split()))
sum=max_subarray_sum(arr)
print(sum) 