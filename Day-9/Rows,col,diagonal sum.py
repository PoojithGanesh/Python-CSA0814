matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows=len(matrix)
cols=len(matrix[0])
rows_sum=[0]*rows
col_sum=[0]*cols
diagonal_sum=0
for i in range(rows):
    for j in range(cols):
        rows_sum[i]+=matrix[i][j]
        col_sum[j]+=matrix[i][j]
        if i==j:
            diagonal_sum+=matrix[i][j]

print("Row sum:",rows_sum)
print("Column sum:",col_sum)
print("Diagonal_sum:", diagonal_sum)
