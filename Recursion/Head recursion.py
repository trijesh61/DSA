#head recursion
def print_n_numbers(n):
    if n==0:
        return
    print_n_numbers(n-1)
    print(n)
print_n_numbers(int(input("Enter n to print n numbers:: ")))    