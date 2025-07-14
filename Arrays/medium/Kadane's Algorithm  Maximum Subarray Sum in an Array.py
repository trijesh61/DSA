#Kadane's Algorithm : Maximum Subarray Sum in an Array

#Problem Statement: Given an integer array arr, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and returns its sum and prints the subarray.

arr=list(map(int,input().split()))
m=0
for i in arr:
    for j in arr:
        if (i+j)>max:
            max=i+j
print(max)
