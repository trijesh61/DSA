#Problem Statement: Given an array Arr[] of integers,
#  rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
#If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

def nextPermutation(arr):
    n = len(arr)
    
    # Step 1: Find the first index 'i' such that arr[i] < arr[i+1], from right
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # Step 2: If such index found, find index 'j' to swap with
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    # Step 3: Reverse the part after index i
    arr[i + 1:] = reversed(arr[i + 1:])
    
    return arr
arr = [1, 3, 2]
print(nextPermutation(arr))  # Output: [2, 1, 3]

arr = [3, 2, 1]
print(nextPermutation(arr))  # Output: [1, 2, 3]
