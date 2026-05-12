# Sum of Min and Max in Python
arr=list(map(int,input().split()))
minimum=float('inf')
maximum=float('-inf')
for i in arr:
    if i<minimum:
        minimum=i
    if i>maximum :
        maximum=i 
print(f"Sum of minimum and maximum is {minimum+maximum}")