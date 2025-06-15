
def find_union(arr1, arr2):
    s = set()
    arr1=set(arr1)
    arr2=set(arr2)
    

    union=arr1.union(arr2)
    return union

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)



