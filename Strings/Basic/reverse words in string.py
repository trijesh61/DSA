#Reverse Words in a String

s=list(input().split())
s1=""
n=len(s)
for i in range(n-1,-1,-1):
    if i==n-1:
        s1=s1+s[i]
    else:
        s1=s1+" "+s[i]
print(s1)
