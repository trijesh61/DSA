#Problem Statement: You are given an array of ‘N’ integers.
#  You need to find the length of the longest sequence which contains the consecutive elements.

def longest_consecutive_numbers_length(arr):
    nums = set(arr)
    longest = 0

    for num in nums:
        # Check if this is the start of a sequence
        if num - 1 not in nums:
            length = 1
            current_num = num
            
            # Count consecutive numbers after current_num
            while current_num + 1 in nums:
                current_num += 1    # increment to next number
                length += 1
            
            longest = max(longest, length)
    
    return longest


arr = list(map(int, input().split()))
l = longest_consecutive_numbers_length(arr)
print(l)