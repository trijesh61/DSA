# Problem Statement: Given an integer N, return all divisors of N.

n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
print(l)