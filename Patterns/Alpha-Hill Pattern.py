n=int(input())
a=ord("A")
for i in range(1,n+1):
    s=a
    print(" "*(n-i),end='')
    for j in range(i):
        print(chr(s),end="")
        s+=1
    for j in range(i-1):
        s-=1
        print(chr(s-1),end='')
        
    print()