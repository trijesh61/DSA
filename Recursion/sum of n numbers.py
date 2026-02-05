def sum(s,n):
    if n==0:
        print(s)
        return
    s=s+n     
    sum(s,n-1)
sum(0,3)