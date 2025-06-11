n = int(input())

# Upper half
for i in range(n):
    print("*" * (i + 1) + " " * ((2 * n) - (2 * i) - 2) + "*" * (i + 1))

# Lower half
for i in range(n - 1, -1, -1):
    print("*" * (i + 1) + " " * ((2 * n) - (2 * i) - 2) + "*" * (i + 1))