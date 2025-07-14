#Kadane's Algorithm : Maximum Subarray Sum in an Array

#Problem Statement: Given an integer array arr, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and returns its sum and prints the subarray.

def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]
    start = end = s = 0  # Track indices for subarray

    for i in range(1, len(arr)):
        if curr_sum + arr[i] < arr[i]:
            curr_sum = arr[i]
            s = i  # Start new subarray
        else:
            curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = s
            end = i

    print("Maximum Subarray:", arr[start:end+1])
    return max_sum
