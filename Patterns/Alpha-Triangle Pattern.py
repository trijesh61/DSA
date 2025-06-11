n=int(input())
e=ord("E")
for i in range(1,n+1):
    s=e+1
    for j in range(i,0,-1):
        print(chr(s-j),end=' ')
    print()