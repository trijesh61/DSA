l=list(map(int,input().split()))
print(f"Orginal List: {l}")
n=len(l)
mid=n//2
i=0
while mid>i:
    l[i],l[n-i-1]=l[n-i-1],l[i]
    i+=1
print(f"Reversed Array: {l}")



