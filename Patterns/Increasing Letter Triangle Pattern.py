n=int(input())
for i in range(1,n+1):
    s=ord("A")
    for j in range(i):
        print(chr(s),end=" ")
        s+=1
    print()