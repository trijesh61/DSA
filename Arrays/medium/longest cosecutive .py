#Problem Statement: You are given an array of ‘N’ integers.
#  You need to find the length of the longest sequence which contains the consecutive elements.

def longet_consecutive_numbers_length(arr):
    nums=set(arr)
    n=len(arr)
    longest=0
    for num in nums:
        if num-1 not in nums:
            length=1
            while num+1 in nums:
                length+=1
            longest=max(longest,length)
    return longest

arr=list(map(int,input().split()))
longet_consecutive_numbers_length(arr)
