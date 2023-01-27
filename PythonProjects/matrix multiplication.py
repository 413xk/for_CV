import copy

n = int(input()) #matrix size
matrixA = [[int(_) for _ in input().split()] for _ in range(n)] #matrix
m = int(input()) #power
matrixB = matrixA

for f in range(m - 1):
    matrixC = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrixC[k][i] += matrixA[k][j] * matrixB[j][i]
    matrixB = copy.deepcopy(matrixC)

matrixC = [[str(_).ljust(2) for _ in range(n)] for _ in range(n)]

for l in range(n):
    print(matrixC[l])

