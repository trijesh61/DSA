#Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

n=int(input())
f=0
for i in range(2,(n//2)+1):
    if n%i==0:
        f+=1
if f==0:
    print("Prime number")
else:
    print("Not a prime Number")