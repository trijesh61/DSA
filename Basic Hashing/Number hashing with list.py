n=[1,2,3,4,1,2,5,7,10,6,5,8,7,4,2,1,3,3,9,5,7] # Numbers with which we need to count
m=[1,3,5,6,111,20,64,7,9] # Numbers to determine the count

l=[0]*11
for i in n:
    l[i]+=1

for i in m:
    if i<0 or i>10:
        print(f"Number {i} not in the list 'n'!!!")
    else:
        print(f"number {i} has repeated for {l[i]} times!")