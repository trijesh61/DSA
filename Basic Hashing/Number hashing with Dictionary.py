n=[1,2,3,4,1,2,5,7,10,6,5,8,7,4,2,1,3,3,9,5,7,111,20,64,7,9] # Numbers with which we need to count
m=[1,3,5,6,111,20,64,7,9] # Numbers to determine the count

d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

for i in m:
    print(f"Number {i} is repeated for {d[i]} times")