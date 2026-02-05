# checking string is palindrome or not
# Reverse of an array using Recursion
def reverse(a,left,right):
    if left>=right:
        return True
    if a[left]!=a[right]:
        return False
    return reverse(a,left+1,right-1)


a="sms"
print(reverse(a,0,len(a)-1))
