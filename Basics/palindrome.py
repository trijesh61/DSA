#Problem Statement: Given an integer N, return true if it is a palindrome else return false.

n=int(input())
rev,temp=0,n
while n>0:
    m=n%10
    rev=rev*10+m
    n=n//10
if temp==rev:
    print("Palindrome number")
else:
    print("Not a Palindrome number")