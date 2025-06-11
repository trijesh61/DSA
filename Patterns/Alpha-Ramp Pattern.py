n=int(input())
m=ord("A")
for i in range(1,n+1):
    for j in range(i):
        print(chr(m),end="")
    print()
    m+=1