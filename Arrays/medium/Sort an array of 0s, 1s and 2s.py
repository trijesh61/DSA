#Problem Statement: Given an array consisting of only 0s, 1s, and 2s.
#Write a program to in-place sort the array without using inbuilt sort functions.
#( Expected: Single pass-O(N) and constant space)

n=int(input())
ar=list(map(int, input().split()))
z,o,t=ar.count(0),ar.count(1),ar.count(2)
ar=[]
ar+=[0]*z
ar+=[1]*o
ar+=[2]*t
print(ar)