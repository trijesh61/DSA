# Check if a number is Armstrong Number or not

n=input()
l,s=len(n),0
for i in n:
    s=s+int(i)**l
if int(n)==s:
    print("Armstrong Number!")
else:
    print("Not an armstrong Number!")