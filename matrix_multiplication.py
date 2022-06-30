# First matrix. M is a list
M = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3]]

# Second matrix. N is a list
N = [[1, 1],
     [2, 2],
     [3, 3],
     [4, 4]]

result=[[0,0],
        [0,0],
        [0,0]]

for i in range(3):
    for j in range(2):
        for k in range(4):
            result[i][j]=result[i][j] + M[i][k] * N[k][j]
for r in result:
    print(r)

