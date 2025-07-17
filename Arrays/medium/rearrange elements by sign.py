#There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
#Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

l=[1,2,-4,-5]

# 1 -4 2 -5
n,p=[],[]
for i in l:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
no=len(l)

neg,pos=0,0
for i in range(no):
    if i%2==0:
        l[i]=p[pos]
        pos+=1
    else:
        l[i]=n[neg]
        neg+=1

print(l)