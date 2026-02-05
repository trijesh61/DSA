# Reverse of an array using Recursion
def reverse(a,left,right):
    if left>=right:
        return
    a[left],a[right]=a[right],a[left]
    reverse(a,left+1,right-1)


a=[1,2,3,4,5]
reverse(a,0,len(a)-1)
print(a)
