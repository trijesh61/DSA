N = int(input())

# Upper half
spaces = 0
for i in range(N):
    print("*" * (N - i) + " " * spaces + "*" * (N - i))
    spaces += 2

# Lower half
spaces = 2 * N - 2
for i in range(1, N + 1):
    print("*" * i + " " * spaces + "*" * i)
    spaces -= 2
