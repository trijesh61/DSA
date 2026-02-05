# Factorial using recursion
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)






n=int(input("Enter number to find the Factorial:: "))
f=factorial(n)
print(f)