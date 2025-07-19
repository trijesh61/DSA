#Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and
#  then return the matrix.

matrix=[[1,1,1],[1,0,1],[1,1,1]]
j,k=[],[]
for i in range(len(matrix)):
    if 0 in matrix[i]:
        j.append(i)
        k.append(matrix.index(matrix[i]))

for i in range(len(k)):
    matrix[j[i],:]=0
    matrix[:,k[i]]=0

print(matrix)