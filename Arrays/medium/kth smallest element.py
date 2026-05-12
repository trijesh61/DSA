# kth smallest element
arr=list(map(int,input().split()))
k=int(input())
arr.sort()
print(f"{k}th Smallest element is {arr[-k]}")