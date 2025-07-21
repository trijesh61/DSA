#Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.


arr=[[1,2,3],[4,5,6],[7,8,9]]

rows,cols=len(arr),len(arr[0])
transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Fill in the transposed matrix
for i in range(rows):
    for j in range(cols):
        transposed[j][i] = arr[i][j]

for col in transposed:
    col.reverse()

print(transposed)