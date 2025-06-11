n=int(input())
for i in range(n,0,-1):
    s=ord("A")
    for j in range(i):
        print(chr(s),end=" ")
        s+=1
    print()