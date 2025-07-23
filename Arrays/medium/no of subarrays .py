from collections import defaultdict

ar = [3, 1, 2, 4]
s = 3
n = len(ar)

prefix_sum = 0
count = 0
freq = defaultdict(int)
freq[0] = 1

i = 0
while i < n:
    prefix_sum += ar[i]

    if (prefix_sum - s) in freq:
        count += freq[prefix_sum - s]

    freq[prefix_sum] += 1
    i += 1

print(count)
