##Problem Statement: Given an array, print all the elements which are leaders. 
# A Leader is an element that is greater than all of the elements on its right side in the array.

arr = [4, 7, 1, 0]
leader=arr[-1]
print(leader)
for i in range(len(arr)-2,-1,-1):
    if arr[i]>leader:
        leader=arr[i]
        print(arr[i])