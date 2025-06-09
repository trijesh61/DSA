"""Problem Statement: Given an integer N, return the number of digits in N."""
n=int(input())
l=0
while n>0:
    l+=1
    n//=10
print(l)