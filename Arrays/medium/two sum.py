def two_sum(arr, target):
    num_map = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return "YES", [num_map[complement] + 1, i + 1]  # 1-based index
        num_map[num] = i
    return "NO", []
arr = [2, 6, 5, 8, 11]
target = 14
res, indices = two_sum(arr, target)
print("Result:", res)
if res == "YES":
    print("Indices:", indices)
