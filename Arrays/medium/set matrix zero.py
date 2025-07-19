#Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and
#  then return the matrix.

matrix=[[1,1,1],[1,0,1],[1,1,1]]

r,c=set(),set()
rows=len(matrix)
cols=len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j]==0:
            r.add(i)
            c.add(j)

for i in r:
    for j in range(cols):
        matrix[i][j]=0

for i in range(rows):
    for j in c:
        matrix[i][j]=0

print(matrix)