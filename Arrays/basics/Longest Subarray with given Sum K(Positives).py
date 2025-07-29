#Longest Subarray with given Sum K(Positives)

a=list(map(int,input().split()))
s=int(input())
l=0
ar=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        b=a[i:j]
        if sum(b)==s and l<len(b):
            l=len(b)
            ar=b
print(ar)   