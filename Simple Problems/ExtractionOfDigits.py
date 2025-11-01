#Extraction of digits from a number

n=int(input())
m=0
while n>0:
    m=n%10
    print(m)
    n//=10