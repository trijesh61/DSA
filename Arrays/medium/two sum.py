#Two Sum : Check if a pair with given sum exists in Array
n=int(input())
ar=list(map(int, input().split()))
target=int(input())
a=[]
tar={}
for i in range(n):
    c=target-ar[i]
    if c in tar:
        a=[tar[c],i]
        break
    tar[ar[i]]=i
print(a)