# It counts the number of digits in a number 

n= int(input())
c=0
while n>0:
    c+=1
    n//=10

print("The Number of digits in number is :",c)