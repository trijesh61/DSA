def quicksort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)

        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    pivot = arr[start]  
    i = start + 1

    for j in range(start + 1, end + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[start], arr[i - 1] = arr[i - 1], arr[start]
    return i - 1

arr = list(map(int, input().split()))
n = len(arr)

quicksort(arr, 0, n - 1)

print("Sorted array:", *arr)
